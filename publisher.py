from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import FastAPIError
from fastapi.responses import JSONResponse
from models.Publisher import Publisher


app = FastAPI()
# publisher = ...


@app.get("/")
def root():
    return {"message": "Hello on publisher!"}


@app.exception_handler(HTTPException)
async def exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=401,
        content={"message": f"catched exception {exc}"},
    )


@app.on_event("startup")
def start_app():
    # global publisher
    publisher = Publisher()
    # publisher.start()
    publisher.simulate()
    # publisher.stop()


# @app.get("/start")
# def start_app():
#     publisher.start()
#     publisher.simulate()
#
#
# @app.get("/stop")
# def stop_app():
#     publisher.stop()


@app.on_event("shutdown")
def stop_app():
    pass
