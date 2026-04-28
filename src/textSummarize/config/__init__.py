from textSummarize import logger
from textSummarize.utils import *
from textSummarize.constants import *


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


            create_dir(self.config.artifact_path)