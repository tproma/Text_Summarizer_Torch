class ConfigurationManager:
    def __init__(
        self,
      confg_filepath = CONFIG_FILE_PATH,
      params_filepath = PARAMS_FILE_PATH):
      
      self.config = read_yaml(config_filepath)
      self.params = read_yaml(params_filepath)
      
      create_directories([self.config.artifacts_root])
