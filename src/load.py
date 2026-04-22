import pandas as pd
from sqlalchemy import create_engine

def load_to_warehouse(): # <--- Fíjate que el paréntesis ahora está vacío
    print("Iniciando carga al Data Warehouse...")

    # Conexión para Docker
    db_url = "mysql+pymysql://root:root@mysql_dw:3306/etl_project"

    try:
        engine = create_engine(db_url)

        
        print("Leyendo archivos procesados...")
        dim_city = pd.read_csv("data/processed/dim_city.csv")
        dim_date = pd.read_csv("data/processed/dim_date.csv")
        dim_source = pd.read_csv("data/processed/dim_source.csv")
        fact_climate_daily = pd.read_csv("data/processed/fact_climate_daily.csv")

        
        print("Cargando tabla: dim_city...")
        dim_city.to_sql("dim_city", con=engine, if_exists="replace", index=False)

        print("Cargando tabla: dim_date...")
        dim_date.to_sql("dim_date", con=engine, if_exists="replace", index=False)

        print("Cargando tabla: dim_source...")
        dim_source.to_sql("dim_source", con=engine, if_exists="replace", index=False)

        print("Cargando tabla: fact_climate_daily...")
        fact_climate_daily.to_sql("fact_climate_daily", con=engine, if_exists="replace", index=False)

        print("Carga completada con éxito.")

    except Exception as e:
        print(f"Error durante la carga: {e}")
        raise