from fastapi import FastAPI


app = FastAPI()
# router_name = "/userservice"
port = 5001


@app.get("/")
def root():
    return {"message": "Go to /get_uuid to get unique user id"}


@app.get("/get_uuid")
def get_uuid():
    pass


@app.get("/publisher")
def publish(id: str = None):
    pass


@app.get("/subscriber")
def subscribe(id: str = None):
    pass


# uvicorn.run("user_service:app", host="0.0.0.0", port=app_port)
