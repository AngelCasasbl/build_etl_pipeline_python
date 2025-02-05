# import needed libraries
from sqlalchemy import create_engine
import pandas as pd
import os
import pymysql
from dotenv import load_dotenv

# enviroment variables
load_dotenv()

pwd    = os.getenv("PGPASS")
uid    = os.getenv("PGUSER")
pgport = os.getenv('PGPORT')
pghost = os.getenv('PGHOST')
pgdb   = os.getenv('PGDB')

mysql_pwd  = os.getenv("MyPASS")
mysql_uid  = os.getenv("MyUSER")
mysql_port = os.getenv('MyPORT')
mysql_host = os.getenv('MyHOST')
mysql_db   = os.getenv('MyDB')

# create connection to mysql database
mysql_engine = create_engine(f"mysql+pymysql://{mysql_uid}:{mysql_pwd}@{mysql_host}:{mysql_port}/{mysql_db}")

# funcion para probar la conexión
def test_connection(engine):
    try:
        with engine.connect() as connection:
            print(f"Conexión exitosa a {connection}")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")


# funcion para extraer datos de mysql y cargarlos en postgres
def extract_mysql():
    try: 
        test_connection(mysql_engine)
        with mysql_engine.connect() as connection:
            query = """SELECT table_name 
                    FROM information_schema.tables 
                    where table_name IN ('employees', 'dept_manager', 'dept_emp', 'salaries', 'titles');"""
            src_tables = pd.read_sql(query, connection)
            
            for table_name in src_tables["TABLE_NAME"]:
                print(f"Extrayendo datos de: {table_name}")
                df = pd.read_sql(f"SELECT * FROM employees.{table_name};", connection)
                
                load_in_postgres(df,table_name)
                
    except Exception as e:
        print(f"Error al extraer la base de datos: {e}")

# funcion para cargar los datos en postgres
def load_in_postgres(df,tbl):
    try:
        rows_imported = 0
        pg_engine = create_engine(f"postgresql://{uid}:{pwd}@{pghost}:{pgport}/{pgdb}")
        test_connection(pg_engine)
        print(f'importing rows {rows_imported} to {rows_imported + len(df)}... for table {tbl}')
        # save df to postgres
        df.to_sql(f'stg_{tbl}', pg_engine, if_exists='replace', index=False, chunksize=100000)
        rows_imported += len(df)
        
        print("Data imported successful")
        
    except Exception as e:
        print("Data load error: " + str(e))

# main function       
try:
    #call extract function
    extract_mysql()
except Exception as e:
    print("Error while extracting data: " + str(e))