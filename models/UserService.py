import datetime, hashlib
from secrets import token_hex
from models.Logger import Logger


class UserService:
    def __init__(self):
        self.logger = Logger("userservice")

    def create_uuid(self) -> str:
        self.logger.add_info("Creating uuid")

        start_token = token_hex(12)
        token = start_token + str(datetime.datetime.now())
        token = hashlib.md5(token.encode()).hexdigest()

        self.logger.add_debug("Uuid: " + token[:2] + "..." + token[-2:])
        self.logger.add_info("Returning uuid")

        return token
