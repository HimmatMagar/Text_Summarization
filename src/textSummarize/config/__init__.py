from textSummarize.utils import *
from textSummarize.constants import *
from textSummarize.entity import *


class ConfigManager:

      def __init__(
                  self,
                  config = config_path,
                  params = params_path,
                  schema = schema_path
      ):
            self.config = read_yaml(config)
            self.params = read_yaml(params)
            self.schema = read_yaml(schema)


            create_dir([self.config.artifact_root])

      
      def get_data_ingestion_config(self) -> DataIngestionConfig:
            config = self.config.data_ingestion
            create_dir([config.root_dir])

            return DataIngestionConfig(
                  root_dir = config.root_dir,
                  source_url = config.source_url,
                  zip_file = config.zip_file,
                  unzip_file = config.unzip_file
            )

      def get_data_validation_config(self) -> DataValidationConfig:
            config = self.config.data_validation
            schema = self.schema.columns
            create_dir([config.root_dir])

            return DataValidationConfig(
                  root_dir=config.root_dir,
                  data_path=config.data_path,
                  status_file=config.status_file,
                  schema=schema
            )