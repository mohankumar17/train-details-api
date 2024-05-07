from app.config import Config
import requests

from app.utils.custom_exception import TRAIN_NOT_FOUND

def get_trains_source_system(trainId):

    host = Config.DB_HOST
    basepath = Config.DB_BASEPATH
    username = Config.DB_USERNAME
    password = Config.DB_PASSWORD

    req_body = {
        "fields": [
            "_id",
            "_rev",
            "trainId",
            "trainName",
            "seatClasses",
            "haltStations"
        ],
        "selector": {
            "trainId": {
                "$eq": trainId
            }
        }
    }

    res = requests.post(url = f"https://{host}{basepath}/_find", 
                        json = req_body,
                        auth = (username, password))
    
    if res.status_code == 200:
        return res.json().get("docs")
    else:
        raise Exception()
    
def get_train_details(trainId):

    train_details_data = get_trains_source_system(trainId)

    if len(train_details_data) == 0:
        raise TRAIN_NOT_FOUND(f"Train details with ID: {trainId} not found in the system")
        
    res_data = train_details_data[0]
    del res_data["_id"]
    del res_data["_rev"]
        
    return res_data
    