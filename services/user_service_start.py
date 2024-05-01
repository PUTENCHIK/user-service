import uvicorn
from src.config import config
from src.connections import get_ip


host = get_ip()
port = config["user_service_port"]

uvicorn.run("user_service:app", host=host, port=port)
