from fastapi import FastAPI
from fastapi.exceptions import FastAPIError

from models.UserService import UserService
from models.Publisher import Publisher
from models.Subscriber import Subscriber


app = FastAPI()
service = UserService()


def message(text: str) -> dict:
    return {"message": text}


@app.get("/")
def root():
    service.logger.add_debug("Request to app's root")
    return message("Go to /get_uuid to get unique user id")


@app.get("/get_uuid")
def get_uuid():
    service.logger.add_debug("Request to app's /get_uuid")
    return {"uuid": service.create_uuid()}


@app.get("/start")
def start_without():
    service.logger.add_warning("Bad usage of /start/{amount}")
    return message("Go to /start/{amount} to start simulation")


@app.get("/start/{amount}")
def start(amount: int):
    service.logger.add_debug("Request to app's /start/{amount}")
    try:
        publisher = Publisher(service.starts_amount)
        service.logger.add_debug("Publisher object created")
    except FastAPIError:
        service.logger.add_error("Impossible to create Publisher")
        return

    try:
        subscriber = Subscriber(service.starts_amount)
        service.logger.add_debug("Subscriber object created")
    except FastAPIError:
        service.logger.add_error("Impossible to create Publisher")
        return

    try:
        subscriber.start()
        subscriber.subscribe()
        publisher.simulate(amount)
    except:
        service.logger.add_error("Simulation was stopped")

    subscriber.stop()

    del publisher
    del subscriber

    service.starts_amount += 1

    return message("Simulation ended")
