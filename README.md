Proyecto: Predicción de Calificaciones en Aplicaciones de Google Play Store
Autora: Valentina Concha Ramírez
Bootcamp Ciencia de Datos – UDD, 2025

1. Introducción
Este proyecto busca responder una pregunta relevante: ¿podemos anticipar si una aplicación móvil tendrá una buena calificación antes de que los usuarios la evalúen? Para lograrlo, se utiliza información histórica de apps y se construye un modelo predictivo, además de una API que permite solicitar predicciones. El objetivo es demostrar un flujo completo profesional: limpieza de datos, exploración, modelado, evaluación y despliegue mediante una API REST.

2. Datos utilizados
El dataset proviene de Kaggle e incluye información sobre categoría, género, tamaño, instalaciones, reseñas, precio, fecha de actualización y rating. La calificación se transformó en una categoría binaria: 1 para rating >= 4.3 y 0 para rating menor a ese valor.

3. Limpieza de datos
El dataset presentaba valores faltantes, columnas con texto que debían convertirse a números, duplicados y formatos inconsistentes. Se completaron valores faltantes, se corrigieron formatos numéricos, se eliminaron duplicados y se crearon nuevas variables logarítmicas (installs_log y reviews_log).

4. Análisis Exploratorio (EDA)
El EDA permitió identificar tendencias importantes: la mayoría de las apps tienen buenas calificaciones, las apps más grandes suelen ser juegos, las instalaciones presentan una distribución muy desigual y las actualizaciones recientes suelen relacionarse con mejores calificaciones.

5. Modelado
Se entrenaron diferentes modelos de predicción: regresión logística, Random Forest, Gradient Boosting y un ensamble final que combinó los modelos anteriores. El ensamble demostró ser el más estable y preciso, por lo que se seleccionó como modelo final.

6. Resultados
El modelo final obtuvo un AUC cercano a 0.79 y un buen desempeño en matriz de confusión. Las predicciones fueron estables y el modelo logró distinguir correctamente entre apps con buena y mala calificación.

7. API REST
Se desarrolló una API con FastAPI que recibe información de una aplicación y devuelve si es probable que tenga una buena calificación junto con el nivel de confianza del modelo.

8. Ejecución de la API
Para ejecutar la API:
uvicorn --app-dir src serve_tabular:app --host 0.0.0.0 --port 8000
La documentación interactiva está disponible en:
http://127.0.0.1:8000/docs

9. Conclusiones
Es posible predecir la calificación de una app utilizando información básica y un modelo bien entrenado. El proyecto demuestra un flujo completo: limpieza, exploración, modelado, evaluación y despliegue de una API.

10. Estructura del proyecto
Proyecto_PlayStore/
├── data/
├── models/
├── outputs/
├── src/
│   ├── train_tabular.py
│   └── serve_tabular.py
└── README.md

11. Cómo utilizar la API
La API permite enviar información de una aplicación y recibir como respuesta una predicción sobre si tendrá una buena calificación. No se necesita saber programar para usarla.

11.1 Iniciar la API
Desde la carpeta del proyecto ejecutar:
uvicorn --app-dir src serve_tabular:app --host 0.0.0.0 --port 8000

11.2 Abrir la interfaz visual
Con la API activa, abrir en el navegador:
http://127.0.0.1:8000/docs
Aquí se despliega una interfaz que permite probar fácilmente la API.

11.3 Usar el botón "Try it out"
En el endpoint /predict, presionar “Try it out” e ingresar los datos de la app. Ejemplo:
{
  "category": "TOOLS",
  "primary_genre": "Tools",
  "content_rating": "Everyone",
  "price_usd": 0.0,
  "installs_num": 500000,
  "size_mb": 15.0,
  "reviews": 2500,
  "upd_year": 2023,
  "upd_month": 10
}

11.4 Interpretar la respuesta
La API responderá algo como:
{
  "prediction": "high_rating",
  "confidence": 0.85
}
“prediction” indica si la app tendrá buena calificación y “confidence” indica qué tan seguro está el modelo (porcentaje).

11.5 ¿Para qué sirve esta API?
Sirve para integrarla a sistemas internos, dashboards, aplicaciones web, procesos automáticos o análisis de mercado. Permite evaluar rápidamente nuevas apps sin esperar a que usuarios reales las califiquen.
