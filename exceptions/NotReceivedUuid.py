class NotReceivedUuid(Exception):
    def __init__(self):
        super(NotReceivedUuid, self).__init__("Failed to get uuid")
