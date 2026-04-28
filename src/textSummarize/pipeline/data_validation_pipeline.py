from textSummarize import logger
from textSummarize.config import ConfigManager
from textSummarize.components.data_validation import DataValidation

STAGE_NAME = "Data Validation Config"

class DataValidationPipeline:
      def __init__(self):
            pass

      def main(self):
            config = ConfigManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(data_validation_config)
            data_validation.validate_column()

if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = DataValidationPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e 