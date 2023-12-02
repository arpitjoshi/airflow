from datetime import datetime, date
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow import DAG
from default_args import args
import pandas as pd


def transform_data():
    print("Todays Date=>", date.today())
    tbl = pd.read_csv('/Users/arpitjoshi/Desktop/airf/output/tld-names-extract.csv')
    tbl_generic = tbl[tbl['Type']=='generic']
    tbl_generic['Date'] = date.today().strftime('%Y-%m-%d')
    tbl_generic.to_csv('/Users/arpitjoshi/Desktop/airf/output/tranform-tld-names-extract.csv', index=False)


with DAG('etl_dag', 
        description='ETL Dag', 
        schedule_interval=None,
        start_date=datetime(2023, 11, 20),
        catchup=False
        ) as dag:
    
    extract_task = BashOperator(
        task_id = 'extract_task',
        bash_command='wget \
            https://datahub.io/core/top-level-domain-names/r/0.csv \
            -O /Users/arpitjoshi/Desktop/airf/output/tld-names-extract.csv'
    )
    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform_data,
        dag=dag)
    
    load_task = BashOperator(
        task_id='load_task',
        bash_command='echo -e ".separator ","\n.import --skip 1 /Users/arpitjoshi/Desktop/airf/output/tranform-tld-names-extract.csv transform_tld_data" | sqlite3 /Users/arpitjoshi/Desktop/airf/output/transform-tld.db',
        dag=dag
    )

    extract_task >> transform_task >> load_task

