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

def taskA():
    print("Arpit Joshi A")

def taskB():
    print("Arpit Joshi B")

def taskC():
    print("Arpit Joshi C")

def taskD():
    print("Arpit Joshi D")

with DAG(
    dag_id='python_operator_exmaple',
    description='python operator exmaple',
    default_args=default_args,
    schedule_interval='@once',
    start_date=days_ago(1),
) as dag:
    taskA = PythonOperator(task_id='taskA', python_callable=taskA)
    taskB = PythonOperator(task_id='taskB', python_callable=taskB)
    taskC = PythonOperator(task_id='taskC', python_callable=taskC)
    taskD = PythonOperator(task_id='taskD', python_callable=taskD)

taskA >> [taskB, taskC] >> taskD
