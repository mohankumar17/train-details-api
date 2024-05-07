from app.config import Config
import requests
from time import localtime, strftime

from app.utils.custom_exception import MIMETYPE_NOT_SUPPORTED
from app.services.get_trains_details import get_trains_source_system

def upsert_train_details(request):

    host = Config.DB_HOST
    basepath = Config.DB_BASEPATH
    username = Config.DB_USERNAME
    password = Config.DB_PASSWORD

    if request.is_json:
        request_body = request.json
    else:
        raise MIMETYPE_NOT_SUPPORTED(f"Request Body's Media Type is not supported. Train details system accepts only application/json MIME Type")
    
    trainId = request_body.get("trainId")
    train_details_data = get_trains_source_system(trainId)
    msg = "inserted"

    if len(train_details_data) > 0:
        msg = "updated"
        request_body["_id"] = train_details_data[0].get("_id")
        request_body["_rev"] = train_details_data[0].get("_rev")
    
    res = requests.post(url = f"https://{host}{basepath}/", 
                        json = request_body,
                        auth = (username, password))
    
    if res.status_code == 200 or res.status_code == 201:
        return {
            "message": f"Train details {msg} successfully",
            "trainId": trainId,
            "dateTime": strftime("%Y-%m-%dT%H:%M:%SZ", localtime())
        }
    else:
        raise Exception()