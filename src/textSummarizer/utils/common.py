import os
import yaml
from box.exceptions import BoxvalueError
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


def read_yaml(path_to_yaml : Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxvalueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
          
