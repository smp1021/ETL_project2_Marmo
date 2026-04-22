from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys


sys.path.append('/opt/airflow')


from src.extract import extract_original_dataset, extract_meteostat
from src.clean import clean_meteostat
from src.transform import transform_datasets
from src.validate import validate_fact_climate_daily
from src.load import load_to_warehouse

default_args = {
    'owner': 'estudiante',
    'start_date': datetime(2026, 4, 22),
}

with DAG('mi_proyecto_clima', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:

    # Extrae
    def paso_extraccion():
        extract_original_dataset()
        extract_meteostat()

    # Limpia y Transforma 
    def paso_transformacion():
        clean_meteostat()
        transform_datasets() 

    # Valida calidad leyendo los CSV
    def paso_validacion():
        validate_fact_climate_daily()

    #  Carga a MySQL leyendo los CSV
    def paso_carga():
        load_to_warehouse()

    # tareas en Airflow
    t1 = PythonOperator(task_id='extraer', python_callable=paso_extraccion)
    t2 = PythonOperator(task_id='transformar', python_callable=paso_transformacion)
    t3 = PythonOperator(task_id='validar', python_callable=paso_validacion)
    t4 = PythonOperator(task_id='cargar', python_callable=paso_carga)

    # orden en el que trabajan
    t1 >> t2 >> t3 >> t4