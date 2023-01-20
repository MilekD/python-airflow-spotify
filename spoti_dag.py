from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from spoti_etl import run_spoti_dag


default_args={
    'owner':'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023,1,11),
    'email':['airflow@example.com'],
    'email_on_failure':False,
    'email_on_retry':False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag=DAG(
    'spotify_dag',
    default_args=default_args,
    description="First ETL code"

)

run_etl=PythonOperator(
    task_id='complete_spotify_etl',
    python_callable=run_spoti_dag(),
    dag=dag
)

run_etl
