
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import Validation
from textSummarizer.logging import logger

class DataValidationTrainingPipeline:
  def __init_(self):
    pass

  def main(self):
    config = ConfigurationManager()
    data_validation_config = config.get_data_validation_config()
    data_validation = DataIngestion(config = data_validation_config)
    data_validation.download_file()
    data_validation.extract_zip_file()
