from flask import Blueprint, request, current_app
import time
import uuid

from app.utils.custom_exception import TRAIN_NOT_FOUND, MIMETYPE_NOT_SUPPORTED
from app.services.get_trains_details import get_train_details
from app.services.upsert_train_details import upsert_train_details
from app.services.delete_train_details import delete_train_details

train_details_bp = Blueprint('train_details', __name__)

# Routers
@train_details_bp.get("/api/trains/<trainId>")
def get_trains_route(trainId):
    return get_train_details(trainId)

@train_details_bp.put("/api/trains/")
def upsert_trains_route():
    return upsert_train_details(request)

@train_details_bp.delete("/api/trains/<trainId>")
def delete_trains_route(trainId):
    return delete_train_details(trainId)

############################################################################
'''
Error Handling
    - Global Error Handler: 500
    - Bad Request: 400
    - Not Found: 404
    - Unsupported Media Type: 415
'''
# Error Handling 
def error_response(errorDetails):
    error_response =  {
        "message": errorDetails.get("message"),
        "description": errorDetails.get("description"),
        "dateTime": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime()),
        "transactionId": str(uuid.uuid4())
    }
    current_app.logger.error(error_response)
    return error_response

@train_details_bp.errorhandler(Exception)
def global_error_handler(error):
    errorDetails = {
        "message": "Train details system server error",
        "description": str(error)
    }
    status_code = 500
    response = error_response(errorDetails)
    return response, status_code

@train_details_bp.errorhandler(TRAIN_NOT_FOUND)
def not_found_error_handler(error):
    errorDetails = {
        "message": "Train details entry not found",
        "description": str(error)
    }
    status_code = 404
    response = error_response(errorDetails)
    return response, status_code

@train_details_bp.errorhandler(MIMETYPE_NOT_SUPPORTED)
def mediatype_error_handler(error):
    errorDetails = {
        "message": "Unsupported Media Type",
        "description": str(error)
    }
    status_code = 415
    response = error_response(errorDetails)
    return response, status_code

'''@train_details_bp.errorhandler()
def validation_error_handler(error):
    errorDetails = {
        "message": "Input data validation failed",
        "description": str(error)
    }
    status_code = 400
    response = error_response(errorDetails)
    return response, status_code'''
