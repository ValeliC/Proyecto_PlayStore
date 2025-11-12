from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import joblib, numpy as np, pandas as pd
from pathlib import Path
import os, sys, types

# Parche por si el modelo guardó funciones en __main__
def impute_nan_with_median(a):
    if isinstance(a, pd.DataFrame): return a.fillna(a.median())
    a = np.array(a, copy=True); m = np.isnan(a)
    if m.any():
        med = np.nanmedian(a, axis=0); inds = np.where(m); a[inds] = np.take(med, inds[1])
    return a
_main = types.ModuleType('__main__'); _main.impute_nan_with_median = impute_nan_with_median
sys.modules['__main__'] = _main

BASE_DIR = Path(os.getcwd())
MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "playstore_ensemble.pkl"
META_PATH  = MODEL_DIR / "model_meta.joblib"

app = FastAPI(title="API Clasificación de Apps Play Store", version="1.0.0")

class AppFeatures(BaseModel):
    category: Optional[str] = None
    primary_genre: Optional[str] = None
    content_rating: Optional[str] = None
    price_usd: Optional[float] = None
    installs_num: Optional[float] = None
    size_mb: Optional[float] = None
    reviews: Optional[float] = None
    upd_year: Optional[int] = None
    upd_month: Optional[int] = None

_model=None; _NUM_COLS=[]; _CAT_COLS=[]
def _load_artifacts():
    global _model,_NUM_COLS,_CAT_COLS
    if _model is None:
        meta = joblib.load(META_PATH)
        _NUM_COLS = meta.get("num_cols", [])
        _CAT_COLS = meta.get("cat_cols", [])
        _model = joblib.load(MODEL_PATH)

def _to_dataframe(p: AppFeatures) -> pd.DataFrame:
    d = p.dict()
    row = {**{c: np.nan for c in _NUM_COLS + _CAT_COLS}, **d}
    row["installs_log"] = np.log1p(row.get("installs_num") or 0)
    row["reviews_log"]  = np.log1p(row.get("reviews") or 0)
    df = pd.DataFrame([row])
    cols = [c for c in _NUM_COLS + _CAT_COLS if c in df.columns]
    return df[cols]

@app.get("/health")
def health():
    try:
        _load_artifacts()
        return {"ok": True, "model_loaded": _model is not None}
    except Exception as e:
        return {"ok": False, "error": str(e)}

@app.post("/predict")
def predict_app(features: AppFeatures):
    _load_artifacts()
    X = _to_dataframe(features)
    proba = _model.predict_proba(X)[0,1]
    pred = int(proba >= 0.5)
    label = "high_rating" if pred else "low_rating"
    return {"prediction": label, "confidence": round(float(proba if pred else 1-proba), 3)}
