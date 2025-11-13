
Proyecto: Predicción de calificaciones en aplicaciones de Google Play Store
Autora: Valentina Concha Ramírez
Bootcamp Ciencia de Datos – UDD, 2025

1. Introducción
Este proyecto busca responder si es posible predecir si una aplicación de Google Play tendrá una buena calificación antes de ser evaluada. Se utiliza información histórica para entrenar un modelo y desplegarlo como una API REST.

2. Datos
Datos públicos de Google Play Store con información sobre categoría, tamaño, número de instalaciones, reseñas, fecha de actualización y rating.

3. Limpieza
Se completaron datos faltantes, se corrigieron formatos, se eliminaron duplicados y se crearon nuevas variables como transforms logarítmicas.

4. Exploración
Se analizaron distribuciones y relaciones entre variables para entender patrones clave.

5. Modelado
Se entrenaron varios modelos y se seleccionó un ensamble de modelos por su mejor rendimiento.

6. Resultados
El ensamble alcanzó un AUC cercano a 0.79 y buen equilibrio en la matriz de confusión.

7. API REST
Se creó una API que permite enviar datos y recibir una predicción del modelo.

8. Conclusiones
Es posible predecir la valoración de una app usando datos históricos y un modelo bien construido.
