import configparser



"""

Initialize the configuration and return it

Args: config_file_path:str: path to .ini config file

"""
def init_config(config_file_path):
	config = configparser.ConfigParser()
	config.read(config_file_path)
	return config


