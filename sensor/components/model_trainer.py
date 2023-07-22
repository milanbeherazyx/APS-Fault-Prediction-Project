from sensor.entity.config_entity import ModelTrainerConfig
from sensor.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
from sensor.logger import logging
from sensor.exception import SensorException
import os,sys 
from xgboost import XGBClassifier
from sklearn.metrics import f1_score
from sensor.utils import load_numpy_array_data,save_object

class ModelTrainer:


    def __init__(self,model_trainer_config:ModelTrainerConfig,
                data_transformation_artifact:DataTransformationArtifact
                ):
        try:
            logging.info(f"{'>>'*20} Model Trainer {'<<'*20}")
            self.model_trainer_config=model_trainer_config
            self.data_transformation_artifact=data_transformation_artifact

        except Exception as e:
            raise SensorException(e, sys) from e

    
    @staticmethod
    def train_model(x,y):
        try:
            xgb_clf =  XGBClassifier()
            xgb_clf.fit(x,y)
            return xgb_clf
        except Exception as e:
            raise SensorException(e, sys) from e

    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        try:
            logging.info("Loading train and test array.")
            train_arr = load_numpy_array_data(file_path=self.data_transformation_artifact.transform_train_path)
            test_arr = load_numpy_array_data(file_path=self.data_transformation_artifact.transform_test_path)


            logging.info(
                "Splitting input and target feature from both train and test arr."
            )
            x_train,y_train = train_arr[:,:-1],train_arr[:,-1]
            x_test,y_test = test_arr[:,:-1],test_arr[:,-1]


            logging.info("Train the model")
            model = ModelTrainer.train_model(x=x_train,y=y_train)

            logging.info("Calculating f1 train score")
            yhat_train = model.predict(x_train)
            f1_train_score  =f1_score(y_true=y_train, y_pred=yhat_train)


            logging.info("Calculating f1 test score")
            yhat_test = model.predict(x_test)
            f1_test_score  =f1_score(y_true=y_test, y_pred=yhat_test)

            logging.info(f"train score:{f1_train_score} and tests score {f1_test_score}")

            logging.info("Checking if our model is underfitting or not")
            if f1_test_score<self.model_trainer_config.expected_score:
                raise Exception(f"Model is not good as it is not able to give \
                expected accuracy: {self.model_trainer_config.expected_score}: model actual score: {f1_test_score}")

            logging.info("Checking if our model is overfiiting or not")
            diff = abs(f1_train_score-f1_test_score)

            if diff>self.model_trainer_config.overfitting_threshold:
                raise Exception(f"Train and test score diff: {diff} is more than overfitting threshold {self.model_trainer_config.overfitting_threshold}")

            #save the trained model
            logging.info("Saving mode object")
            save_object(file_path=self.model_trainer_config.model_path, obj=model)


            #prepare artifact
            logging.info("Prepare the artifact")
            model_trainer_artifact  = ModelTrainerArtifact(model_path=self.model_trainer_config.model_path, 
            f1_train_score=f1_train_score, f1_test_score=f1_test_score)
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact
        except Exception as e:
            raise SensorException(e, sys) from e

