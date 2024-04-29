import uvicorn, socket
from user_service import port


host = socket.gethostbyname(socket.gethostname())

uvicorn.run("user_service:app", host="0.0.0.0", port=port)
