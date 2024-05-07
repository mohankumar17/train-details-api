from app.config import Config
import requests
from time import localtime, strftime

from app.services.get_trains_details import get_trains_source_system
from app.utils.custom_exception import TRAIN_NOT_FOUND

def delete_train_details(trainId):

    host = Config.DB_HOST
    basepath = Config.DB_BASEPATH
    username = Config.DB_USERNAME
    password = Config.DB_PASSWORD

    train_details_data = get_trains_source_system(trainId)

    if len(train_details_data) > 0:
        doc_id = train_details_data[0].get("_id")
        rev_id = train_details_data[0].get("_rev")
    else:
        raise TRAIN_NOT_FOUND(f"Train details with ID: {trainId} not found in the system")
    
    res = requests.delete(url = f"https://{host}{basepath}/{doc_id}?rev={rev_id}", 
                        auth = (username, password))
    
    if res.status_code == 200:
        return {
            "message": f"Train details deleted successfully",
            "trainId": trainId,
            "dateTime": strftime("%Y-%m-%dT%H:%M:%SZ", localtime())
        }
    else:
        raise Exception()