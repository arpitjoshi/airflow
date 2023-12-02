from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG
from default_args import args

with DAG('extract_dag', 
        description='Extract Dag', 
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