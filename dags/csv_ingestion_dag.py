from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from airflow.utils.dates import days_ago
import os
from custom_scripts.data_loader import process_csv
from custom_scripts.db_connector import insert_dataframe_to_db

DATA_DIR = "/opt/airflow/data"  

def process_csv_task(file_name):
    file_path = os.path.join(DATA_DIR, file_name)
    result = process_csv(file_path)
    return result

def insert_data_task(file_name):
    file_path = os.path.join(DATA_DIR, file_name)
    result = process_csv(file_path)
    df = result['dataframe']
    table_name = result['table_name']
    insert_dataframe_to_db(df, table_name)

default_args = {
    'owner': 'user',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG(
    'csv_ingestion_pipeline',
    default_args=default_args,
    description='Ingest CSVs into PostgreSQL',
    schedule_interval=None, 
    start_date=days_ago(1),
    catchup=False,
) as dag:

    check_for_files = FileSensor(
        task_id='check_for_new_files',
        filepath=DATA_DIR,
        poke_interval=30,
        timeout=600,
    )

    process_csv_files = PythonOperator(
        task_id='process_csv_files',
        python_callable=process_csv_task,
        op_kwargs={'file_name': 'dataHeader.csv'},
    )

    insert_to_db = PythonOperator(
        task_id='insert_to_db',
        python_callable=insert_data_task,
        op_kwargs={'file_name': 'dataHeader.csv'},
    )

    check_for_files >> process_csv_files >> insert_to_db
