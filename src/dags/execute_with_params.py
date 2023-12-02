import time
from datetime import datetime, timedelta

from airflow.utils.dates import days_ago
from airflow.decorators import dag, task
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'Arpit J'
}

def taskA(name):
    print("taskA -> " + name)

def taskB(name, city):
    print("taskB -> " + name + " " + city)

with DAG(
    dag_id='python_operator_with_params',
    description='python operator with params',
    default_args=default_args,
    schedule_interval='@once',
    start_date=days_ago(1),
) as dag:
    taskA = PythonOperator(
        task_id='taskA', 
        python_callable=taskA,
        op_kwargs={'name': 'Arpit J'}
        )
    taskB = PythonOperator(
        task_id='taskB', 
        python_callable=taskB,
        op_kwargs={'name': 'Arpit J', 'city': 'GGN'}
        )
        

taskA >> taskB
