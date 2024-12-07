from typing import Dict
from .http_unprocessable_entity import HttpUnprocessableEntityError

def handle_errors(error: Exception) -> Dict:
  if isinstance(error, (HttpUnprocessableEntityError)):
    return {
      "status_code": error.status_code,
      "body": {
        "errors": [{
          "title": error.name,
          "details": error.message
        }]
      }
    }
  
  return {
    "status_code": 500,
      "body": {
        "errors": [{
          "title": "ServerError",
          "details": str(error)
        }]
      }
  }