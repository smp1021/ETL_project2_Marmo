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

Ejemplos de validaciones:

●	No valores nulos en columnas clave

●	Rangos válidos de temperatura

●	Tipos de datos correctos

●	Fechas válidas
 Esto asegura que el pipeline no cargue datos corruptos o inconsistentes.

________________________________________

 4. Load

Guardado de datos procesados en:

data/processed/

●	Listos para análisis o dashboards

________________________________________

 5. Orquestación ( Airflow)
El pipeline está automatizado con Apache Airflow.

Se definen DAGs que ejecutan:

1.	Extract

2.	Transform

3.	Validate

4.	Load

Ventajas:

●	Automatización del flujo

●	Ejecución programada

●	Monitoreo de tareas

●	Manejo de errores

________________________________________

 
 Cómo correr el proyecto

1. Clonar el repositorio

git clone https://github.com/smp1021/ETL_project2_Marmo

cd ETL_project2_Marmo


________________________________________

2. Crear entorno virtual

Windows

python -m venv venv

venv\Scripts\activate


Mac/Linux

python3 -m venv venv

source venv/bin/activate


________________________________________

3. Instalar dependencias

pip install -r requirements.txt


________________________________________

4. Configurar API Key

Ir a:

 https://rapidapi.com/meteostat/api/meteostat


●	Crear cuenta

●	Dar “Subscribe”

●	Copiar API key

Luego en:

etl/extract.py


Reemplazar:

"x-rapidapi-key": "TU_API_KEY"

________________________________________

5. Ejecutar el pipeline manualmente

python etl/main.py

________________________________________

 Ejecutar con Airflow

Levantar contenedores (Docker)

docker-compose up --build

________________________________________

Acceder a Airflow

Ir a:

http://localhost:8080


Usuario por defecto:

airflow / airflow

________________________________________

Ejecutar DAG

●	Buscar el DAG del proyecto

●	Activarlo

●	Ejecutarlo manualmente o programarlo
________________________________________

Estructura del proyecto

ETL_project2_Marmo/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── dags/                # DAGs de Airflow
├── great_expectations/  # Validaciones de datos
├── notebooks/
├── docker-compose.yml
├── requirements.txt
└── README.md


________________________________________

 Tecnologías utilizadas

●	Python 

●	Pandas

●	Requests

●	Apache Airflow

●	Great Expectations

●	Docker 

●	APIs (RapidAPI - Meteostat)
________________________________________
 
 Notas importantes

●	La API key es obligatoria para el extract

●	Great Expectations evita cargar datos inválidos

●	Airflow automatiza todo el pipeline

●	Los datos finales quedan en data/processed
________________________________________