import datetime
import hashlib
from secrets import token_hex

from models.Logger import Logger


class UserService:
    def __init__(self):
        self.logger = Logger("userservice")
        self.starts_amount = 0

    def create_uuid(self) -> str:
        self.logger.add_debug("Creating uuid")

        start_token = token_hex(12)
        token = start_token + str(datetime.datetime.now())
        token = hashlib.md5(token.encode()).hexdigest()

        self.logger.add_info("Uuid: " + token[:2] + "..." + token[-2:])
        self.logger.add_debug("Returning uuid")

        return token
