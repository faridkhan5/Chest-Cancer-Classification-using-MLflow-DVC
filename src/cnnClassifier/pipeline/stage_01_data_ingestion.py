from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger


STAGE_NAME = 'Data Ingestion stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        """
        run our entire pipeline
        """
        #initialize obj to read configuration
        config = ConfigurationManager()
        
        #retrieve the data ingestion config using the resp method
        data_ingestion_config = config.get_data_ingestion_config()

        #create instance of DataIngestion class with the above config
        data_ingestion = DataIngestion(config=data_ingestion_config)

        #perform the data ingestion tasks
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e