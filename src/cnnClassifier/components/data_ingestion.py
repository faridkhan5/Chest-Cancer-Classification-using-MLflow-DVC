import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    """
    handle the data ingestion process

    Args:
        config(DataIngestionConfig): DataIngestionConfig object
    """
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_file(self) -> str:
        """
        fetch data from remote URL
        """
        try:
            #fetch data
            dataset_url = self.config.source_URL
            #save downloaded file to the local data file path
            zip_download_dir = self.config.local_data_file
            os.makedirs('artifacts/data_ingestion', exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, zip_download_dir)
            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e
        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        extracts the zip file into the data dir
        func returns None
        """
        unzip_path = self.config.unzip_dir
        #create unzip dir if it doesn't exist
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)