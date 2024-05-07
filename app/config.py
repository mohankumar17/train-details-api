import yaml
import logging

class Config:
    with open("config/dev.yaml") as config_file:
        properties = yaml.safe_load(config_file)
    
    HTTP_HOST = properties["http"]["host"]
    HTTP_PORT = properties["http"]["port"]

    DB_HOST = properties["ibm"]["cloudantDB"]["host"]
    DB_BASEPATH = properties["ibm"]["cloudantDB"]["basePath"]
    DB_USERNAME = properties["ibm"]["cloudantDB"]["username"]
    DB_PASSWORD = properties["ibm"]["cloudantDB"]["password"]

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)