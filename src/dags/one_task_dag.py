'''One task dag'''
from airflow.operators.bash import BashOperator
from airflow import DAG
from default_args import args


with DAG(
    dag_id='one_dag_task',
    description='One Dag Task',
    schedule_interval=None,
    default_args=args
) as dag:
    task1 = BashOperator(
        task_id='one_task',
        bash_command='echo "Hello Learnings" > /Users/arpitjoshi/Desktop/airf/output/one_task.txt',
        dag=dag
    )