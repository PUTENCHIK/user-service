from models.Publisher import Publisher
from models.UserService import UserService


service = UserService()
print(service.create_uuid())
