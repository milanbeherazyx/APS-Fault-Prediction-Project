from sensor.utils import dump_csv_file_to_mongodb_collection
from sensor.exception import SensorException
from sensor.logger import logging
import os,sys
def storing_record_in_mongo():
    try:
        file_path="aps_failure_training_set1.csv"
        database_name = "sensor"
        collection_name = "sensor_readings"
        dump_csv_file_to_mongodb_collection(file_path, database_name, collection_name)
    except Exception as e:
        raise e

if __name__=="__main__":
    storing_record_in_mongo()