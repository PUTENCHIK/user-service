import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import FastAPIError

from src.config import config
from src.connections import get_ip
from models.UserService import UserService
from models.Publisher import Publisher
from models.Subscriber import Subscriber


app = FastAPI()
service = UserService()
# router_name = "/userservice"


def message(text: str) -> dict:
    return {"message": text}


@app.get("/")
def root():
    return message("Go to /get_uuid to get unique user id")


@app.get("/get_uuid")
def get_uuid():
    return {"uuid": service.create_uuid()}


@app.get("/start")
def start_without():
    return message("Go to /start/{amount} to start simulation")


@app.get("/start/{amount}")
# @app.on_event("startup")
def start(amount: int):
    try:
        publisher = Publisher()
        service.logger.add_debug("Publisher object created")
    except FastAPIError:
        service.logger.add_error("Impossible to create Publisher")
        return

    try:
        subscriber = Subscriber()
        service.logger.add_debug("Subscriber object created")
    except FastAPIError:
        service.logger.add_error("Impossible to create Publisher")
        return

    try:
        subscriber.start()
        subscriber.subscribe()
        # subscriber.simulate(0)
        publisher.simulate(amount)
    except:
        service.logger.add_error("Simulation was stopped")

    subscriber.stop()

    del publisher
    del subscriber

    return message("Simulation ended")


if __name__ == "__main__":
    try:
        service.logger.add_info("Starting app")
        uvicorn.run(app, host="0.0.0.0", port=config['user_service_port'],)
        service.logger.add_info("Normal stop app")
    except:
        service.logger.add_error("Force stop app")
