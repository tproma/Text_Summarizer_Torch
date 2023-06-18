from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try:
  logger.info(f" >>>>>>> stage  {STAGE_NAME} started <<<<<<<<")
