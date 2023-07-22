from sensor.pipeline.batch_prediction import SensorBatchPrediction
from sensor.entity.config_entity import BatchPredictionConfig



if __name__=="__main__":
    config = BatchPredictionConfig()
    sensor_batch_prediction = SensorBatchPrediction(batch_config=config)
    sensor_batch_prediction.start_prediction()