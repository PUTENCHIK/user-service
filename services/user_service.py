from fastapi import FastAPI
# from models.UserService import UserService
from ..models.UserService import UserService


app = FastAPI()
service = UserService()
# router_name = "/userservice"


@app.get("/")
def root():
    return {"message": "Go to /get_uuid to get unique user id"}


@app.get("/get_uuid")
def get_uuid():
    return {"uuid": service.create_uuid()}
