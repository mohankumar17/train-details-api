from app.config import Config

def database_connect():

    host = Config.DB_HOST
    basepath = Config.DB_BASEPATH
    username = Config.DB_USERNAME
    password = Config.DB_PASSWORD

    dbConn = ""

    return dbConn