# read data from different data sources, big data team can have data in multiple sources e.g. hadoop, mongo db and they are storing it somewhere.
# we have to read data from differt data sources, data sources can be of different types e.g. online, offline, live.
# after data ingestion only we perform data transformation.
# dataclasss is an interesting way to define class variables(while we generally define class variables, we define then in __init__, but 
# using dataclass decorator as below we can beautifully define class variables).
# if you are just defining variables in class then you can use dataclass, other wise you can use old method __init__.

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts', "train.csv")
    test_data_path:str=os.path.join('artifacts', "test.csv")
    raw_data_path:str=os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        try:
            #you can read data here from any db, api or somewhere else.
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe.')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            logging.info('Train test split initiated')
            train_set, test_set=train_test_split(df,test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion of data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
# whenever we want to run this file seperately, we can include below code in this file and using terminal run command:- python src/components/data_ingestion.py            
if __name__=="main":
    obj=DataIngestion()
    obj.initiate_data_ingestion()            