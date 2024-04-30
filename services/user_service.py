from fastapi import FastAPI
from models.UserService import UserService


app = FastAPI()
service = UserService()
# router_name = "/userservice"
port = 5001


@app.get("/")
def root():
    service.logger.add_info("")
    return {"message": "Go to /get_uuid to get unique user id"}


@app.get("/get_uuid")
def get_uuid():
    return {"uuid": service.create_uuid()}
