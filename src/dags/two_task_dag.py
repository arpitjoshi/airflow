'''Two task DAG'''
from airflow.operators.bash import BashOperator
from airflow import DAG
from default_args import args

with DAG(
    dag_id='two_task_dag', 
    description='two task dag', 
    schedule_interval=None,
    default_args=args
    ) as dag:
    t0 = BashOperator(
        task_id = 'bash_task_0',
        bash_command='echo "This is the first bash task"'
    )
    t1 = BashOperator(
        task_id = 'bash_task_1',
        bash_command='echo "Sleeping for 5 secs" && sleep 5 && echo "Now starting the second bash task"'
    )

    t0 >> t1