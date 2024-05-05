import uvicorn
from src.config import config
from src.connections import get_ip


# host = get_ip()
host = "0.0.0.0"
port = config["publisher_port"]

uvicorn.run("publisher:app", host=host, port=port)
