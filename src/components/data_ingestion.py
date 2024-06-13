import os
import sys
import pandas as pd
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split



class DataIngestionConfig():
    #configurations
    train_data_path = os.path.join("artifacts","train.csv")
    test_data_path = os.path.join("artifacts","test.csv")
    raw_data_path = os.path.join("artifacts","raw.csv")

class DataIngestion():
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        try:
            df = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/ML_Project_with_ContinuesTraining/main/notebooks/data/gemstone.csv")
            logging.info("data reading from pandas dataframe is completed")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            #artifacts
            df.to_csv(self.ingestion_config.raw_data_path)

            #split the data for training and testing
            train_set, test_set = train_test_split(df,test_size=0.25,random_state=42)
            logging.info("train and test data split is completed")

            #save the train and test data into csv
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("data ingestion is successfully completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            raise Exception
        
if __name__=="__main__":
    data_ingestion=DataIngestion()
    data_ingestion.initiate_data_ingestion()