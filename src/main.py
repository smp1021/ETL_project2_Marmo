from extract import extract_original_dataset, extract_meteostat
from clean import clean_meteostat
from transform import transform_datasets
from load import load_to_warehouse
from validate import validate_fact_climate_daily

def main():
    print(" INICIANDO PIPELINE ETL...")

    # Extracción
    print("\n--- FASE 1: EXTRACCIÓN ---")
    extract_original_dataset()
    extract_meteostat()

    # Limpieza
    print("\n--- FASE 2: LIMPIEZA ---")
    clean_meteostat()

    # Transformación
    print("\n--- FASE 3: TRANSFORMACIÓN ---")
    # Guardamos los 4 dataframes que retorna la función en variables
    dim_city, dim_date, dim_source, fact_climate_daily = transform_datasets()

    # Carga al Data Warehouse
    print("\n--- FASE 4: CARGA ---")
    # Enviamos las variables recién creadas a la base de datos
    load_to_warehouse(dim_city, dim_date, dim_source, fact_climate_daily)

    # Validación
    print("\n--- FASE 5: VALIDACIÓN ---")
    validate_fact_climate_daily()

    print("\n ¡PIPELINE ETL EJECUTADO CON ÉXITO EN SU TOTALIDAD!")

if __name__ == "__main__":
    main()