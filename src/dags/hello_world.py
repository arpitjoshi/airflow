from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'Arpit J'
}

dag = DAG(
    dag_id='hello-world', 
    description='Hello World',
    start_date=days_ago(1) ,
    schedule_interval=None,
    default_args=default_args
    )

t1 = BashOperator(
    task_id='t1',
    bash_command='echo "Hello World"',
    dag=dag
)
t2 = BashOperator(
    task_id='t2',
    bash_command='echo "Welcome to World"',
    dag=dag
)

t1 >> t2
