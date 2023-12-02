''' Load DAG '''
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG

with DAG('load_dag',
    start_date=datetime(2023, 11, 1),
    schedule_interval=None,
    catchup=False) as dag:

    load_task = BashOperator(
        task_id='load_task',
        bash_command='echo -e ".separator ","\n.import --skip 1 /Users/arpitjoshi/Desktop/airf/output/tranform-tld-names-extract.csv transform_tld_data" | sqlite3 /Users/arpitjoshi/Desktop/airf/output/transform-tld.db',
        dag=dag
    )

