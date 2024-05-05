import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.config import config
from src.connections import get_ip
from models.UserService import UserService
from models.Publisher import Publisher
from models.Subscriber import Subscriber


app = FastAPI()
service = UserService()
# router_name = "/userservice"


@app.get("/")
def root():
    return {"message": "Go to /get_uuid to get unique user id"}


@app.get("/get_uuid")
def get_uuid():
    return {"uuid": service.create_uuid()}


# @app.get("/start")
@app.on_event("startup")
def start():
    publisher = Publisher()
    service.logger.add_debug("Publisher object created")
    subscriber = Subscriber()
    service.logger.add_debug("Subscriber object created")

    publisher.simulate()


if __name__ == "__main__":
    try:
        uvicorn.run(app, host="0.0.0.0", port=config['user_service_port'],)
        service.logger.add_info("Normal stop app")
    except KeyboardInterrupt:
        service.logger.add_error("Force stop app")
