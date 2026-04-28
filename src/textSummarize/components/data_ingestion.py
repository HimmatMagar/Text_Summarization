import os
import gdown
import zipfile
import urllib.request as r
from textSummarize import logger
from textSummarize.entity import DataIngestionConfig


class DataIngestion:
      def __init__(self, config: DataIngestionConfig):
            self.config = config

      def download_file(self):
            if not os.path.exists(self.config.zip_file):
                  file_id = "1vmsJgp69jH_pLFh1J4ZXAkqjGcMP-MhD"
                  
                  gdown.download(
                        id=file_id,
                        output=self.config.zip_file,
                        quiet=False
                  )

                  logger.info(f"Downloaded file to {self.config.zip_file}")
            else:
                  logger.info("File already exists")


      def extract_zip_file(self):
            file = self.config.unzip_file
            os.makedirs(file, exist_ok=True)
            with zipfile.ZipFile(self.config.zip_file, 'r') as f:
                  f.extractall(file)