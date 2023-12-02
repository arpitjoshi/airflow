from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'Arpit J'
}

dag = DAG(
    dag_id='multiple_dags', 
    description='Multiple Dags',
    start_date=days_ago(1) ,
    schedule_interval=timedelta(days=1),
    tags=["multiple"],
    default_args=default_args,
    template_searchpath='/Users/arpitjoshi/Desktop/airf/src/dags/shell_scripts'
    )

taskA = BashOperator(task_id='taskA', bash_command='taskA.sh', dag=dag)
taskB = BashOperator(task_id='taskB', bash_command='taskB.sh', dag=dag)
taskC = BashOperator(task_id='taskC', bash_command='taskC.sh', dag=dag)
taskD = BashOperator(task_id='taskD', bash_command='taskD.sh', dag=dag)
taskE = BashOperator(task_id='taskE', bash_command='taskE.sh', dag=dag)
taskF = BashOperator(task_id='taskF', bash_command='taskF.sh', dag=dag)
taskG = BashOperator(task_id='taskG', bash_command='taskG.sh', dag=dag)


taskA >> [taskB, taskC, taskD]
taskB >> taskE
taskC >> taskF
taskD >> taskG