import time
from datetime import datetime, timedelta

from airflow.utils.dates import days_ago
from airflow.decorators import dag, task
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Arpit J'
}

# with DAG(
#     dag_id='dag_with_taskflow',
#     description='Dag using Taskflow Python API',
#     default_args=default_args,
#     schedule_interval='@once',
#     start_date=days_ago(1),
#     tags=['dependecies', 'python', 'taskflow'],
#     ) as dag:
#     task1 = BashOperator(
#         task_id='one_task',
#         bash_command='echo "Hello Learnings"',
#         dag=dag
#     )

@dag(dag_id='dag_with_taskflow',
    description='Dag using Taskflow Python API',
    default_args=default_args,
    schedule_interval='@once',
    start_date=days_ago(1),
    tags=['dependecies', 'python', 'taskflow'],)
def dag_with_taskflow_api():
    
    @task
    def task_one():
        print("Arpit Joshi 1")


    @task
    def task_two():
        time.sleep(10)
        print("Arpit Joshi 2")

    task_one() >> task_two()


dag_with_taskflow_api()