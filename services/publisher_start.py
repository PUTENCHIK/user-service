import uvicorn
from src.config import config
from src.connections import get_ip


host = get_ip()
port = config["publisher_port"]

uvicorn.run("publisher:app", host=host, port=port)
