from datetime import datetime, date
from airflow.operators.python import PythonOperator
from airflow import DAG
import pandas as pd


def transform_data():
    print("Todays Date=>", date.today())
    tbl = pd.read_csv('/Users/arpitjoshi/Desktop/airf/output/tld-names-extract.csv')
    tbl_generic = tbl[tbl['Type']=='generic']
    tbl_generic['Date'] = date.today().strftime('%Y-%m-%d')
    tbl_generic.to_csv('/Users/arpitjoshi/Desktop/airf/output/tranform-tld-names-extract.csv', index=False)

with DAG('transform_dag', 
         description="Transform DAG", 
         catchup=False,
         start_date=datetime(2023, 11, 1),
         schedule_interval=None) as dag:
    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform_data,
        dag=dag)
