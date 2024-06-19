from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'test_dag',
    default_args=default_args,
    description='A simple test DAG',
    schedule_interval=timedelta(minutes=5),  # 5분마다 실행
    start_date=datetime.now() + timedelta(minutes=5),  # 현재 시간으로부터 5분 뒤에 시작
    catchup=False,
)

t1 = DummyOperator(
    task_id='dummy_task',
    dag=dag,
)
