
ETL Project 2 – Climate Data Pipeline (IDEAM + Meteostat)

 
 Descripción del proyecto


Este proyecto implementa un pipeline ETL automatizado para integrar, limpiar y validar datos climáticos provenientes de múltiples fuentes en Colombia.
Se combinan:


●	Datos históricos locales (IDEAM)
●	Datos externos desde API (Meteostat vía RapidAPI)
El pipeline permite generar datasets confiables para análisis, KPIs y visualización.


________________________________________
 Arquitectura del proyecto
El flujo completo del proyecto es:
Extract → Transform → Validate → Load → Analyze

 
 1. Extract

●	Lectura de archivos CSV (IDEAM)

●	Consumo de API Meteostat (temperatura, precipitación, etc.)
 
 2. Transform

●	Limpieza de columnas (lowercase, espacios)

●	Conversión de fechas

●	Estandarización de formatos

●	Integración de datasets

●	Creación de variables como date
 
 3. Validate ( Great Expectations)


Aquí es donde el proyecto se vuelve serio:

Se usa Great Expectations para validar la calidad de los datos antes de cargarlos.
