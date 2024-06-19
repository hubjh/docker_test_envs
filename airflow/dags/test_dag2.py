from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'test_dag2',
    default_args=default_args,
    description='A simple test DAG 2',
    schedule_interval=timedelta(minutes=10),  # 10분마다 실행
    start_date=datetime(2024, 6, 13, 0, 0, 0),  # 2024년 6월 13일 0시부터 시작
    catchup=False,
)

t1 = DummyOperator(
    task_id='dummy_task2',
    dag=dag,
)
