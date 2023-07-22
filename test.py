from sensor.utils import dump_csv_file_to_mongodb_collection
from sensor.exception import SensorException
from sensor.logger import logging
import os,sys
def storing_record_in_mongo():
    try:
        file_path=r"/home/milanbeherazyx/Data Science/sensor_fault_detection/aps_failure_training_set1.csv"
        database_name = "Project"
        collection_name = "sensor_readings"
        dump_csv_file_to_mongodb_collection(file_path, database_name, collection_name)
    except Exception as e:
        raise e


def test_exception_and_logger():
    try:
        x=1/0
    except Exception as e:
        raise SensorException(e, sys) from e

if __name__=="__main__":
    try:
        test_exception_and_logger()
    except Exception as e:
        logging.info(f"error: {e}")
        print(e)