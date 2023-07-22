from sensor.entity.config_entity import BatchPredictionConfig
from sensor.exception import SensorException
from sensor.logger import logging
import os,sys 
from sensor.utils import load_object
from sensor.ml.model_resolver import ModelResolver
import pandas as pd
from datetime import datetime
import numpy as np
import shutil
import os 


from glob import glob 
class SensorBatchPrediction:

    def __init__(self,batch_config:BatchPredictionConfig):
        try:
            self.batch_config=batch_config
        except Exception as e:
            raise SensorException(e,sys) from e

    def start_prediction(self):
        try:
            input_files = glob(f"{self.batch_config.inbox_dir}/*.csv")

            if not input_files:
                logging.info("No file found hence closing the batch prediction")
                return None 

            model_resolver = ModelResolver()

            logging.info("Loading transformer to transform dataset")
            transformer = load_object(file_path=model_resolver.get_latest_transformer_path())

            logging.info("Loading model to make prediction")
            model = load_object(file_path=model_resolver.get_latest_model_path())

            logging.info("Target encoder to convert predicted column into categorical")
            target_encoder = load_object(file_path=model_resolver.get_latest_target_encoder_path())

            for file_path in input_files:
                logging.info(f"Reading file : {file_path}")
                df = pd.read_csv(file_path)
                df.replace({"na":np.NAN},inplace=True)

                input_feature_names =  list(transformer.feature_names_in_)
                input_arr = transformer.transform(df[input_feature_names])

                prediction = model.predict(input_arr)
                cat_prediction = target_encoder.inverse_transform(prediction)
                df["prediction"]=prediction
                df["cat_pred"]=cat_prediction

                file_name = os.path.basename(file_path)
                file_name = file_name.replace(".csv", f"_{datetime.now().strftime('%m%d%Y__%H%M%S')}.csv")
                prediction_file_path = os.path.join(self.batch_config.outbox_dir,file_name)

                logging.info(f"Saving prediction  file : {prediction_file_path}")
                df.to_csv(prediction_file_path,index=False,header=True)

                archive_file_path = os.path.join(self.batch_config.archive_dir,file_name)


                shutil.copyfile(src=file_path, dst=archive_file_path)
                logging.info(f"Copying input file into archive: {archive_file_path}")
                logging.info("Removing file from inbox")
                os.remove(file_path)

        except Exception as e:
            raise SensorException(e, sys) from e