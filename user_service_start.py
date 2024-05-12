import uvicorn
from src.config import config
from user_service import app


host = "0.0.0.0"
port = config["user_service_port"]

try:
    uvicorn.run(app, host=host, port=port)
except KeyboardInterrupt:
    exit()
