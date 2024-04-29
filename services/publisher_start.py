import uvicorn, socket
from publisher import port


host = socket.gethostbyname(socket.gethostname())

uvicorn.run("publisher:app", host="0.0.0.0", port=port)
