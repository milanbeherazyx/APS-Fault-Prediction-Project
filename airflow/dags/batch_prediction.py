from asyncio import tasks
import json
from textwrap import dedent
import pendulum
import os
from airflow import DAG
from airflow.operators.python import PythonOperator

from sensor.pipeline.batch_prediction import BatchPredictionConfig,SensorBatchPrediction

config = BatchPredictionConfig()
with DAG(
    'batch_prediction',
    default_args={'retries': 2},
    # [END default_args]
    description='Sensor Fault Detection',
    schedule_interval="@weekly",
    start_date=pendulum.datetime(2022, 12, 18, tz="UTC"),
    catchup=False,
    tags=['example'],
) as dag:
    def download_files(**kwargs):
        bucket_name = os.getenv("BUCKET_NAME")
        input_dir = "/app/input_files"
        #creating directory
        os.makedirs(input_dir,exist_ok=True)
        os.system(f"aws s3 sync s3://{bucket_name}/inbox {config.inbox_dir}")

    def batch_prediction(**kwargs):
        from sensor.pipeline.batch_prediction import BatchPredictionConfig,SensorBatchPrediction
        config = BatchPredictionConfig()
        sensor_batch_prediction = SensorBatchPrediction(batch_config=config)
        sensor_batch_prediction.start_prediction()
       
    def upload_files(**kwargs):
        bucket_name = os.getenv("BUCKET_NAME")
        os.system(f"aws s3 sync {config.archive_dir} s3://{bucket_name}/archive")
        os.system(f"aws s3 sync {config.outbox_dir} s3://{bucket_name}/outbox")


    download_input_files  = PythonOperator(
            task_id="download_file",
            python_callable=download_files

    )

    generate_prediction_files = PythonOperator(
            task_id="prediction",
            python_callable=batch_prediction

    )

    upload_prediction_files = PythonOperator(
            task_id="upload_prediction_files",
            python_callable=upload_files

    )

    download_input_files >> generate_prediction_files >> upload_prediction_files