import time
from random import choice
from models.MyClient import MyClient


class Publisher(MyClient):
    def __init__(self, number):
        super(Publisher, self).__init__(f"publisher{number}")
        self.connect()

    def publish(self, text: str):
        self.logger.add_info("Published message: " + text)
        self.client.publish(Publisher.path, text)

    def simulate(self, amount: int = 5):
        self.logger.add_debug(f"Start simulating publisher's work")
        try:
            self.start()
            for _ in range(amount):
                delay = Publisher.random_publish_delay()
                self.publish(Publisher.random_message())
                self.logger.add_debug(f"After publish delay: {delay}")
                time.sleep(delay)
        except KeyboardInterrupt:
            self.logger.add_error(f"Simulating was canceled")
            self.stop()
        finally:
            self.logger.add_info("Simulating ended")
            self.stop()

    @staticmethod
    def random_message() -> str:
        adjectives = "Healing Iron Magic Dragon Wraith Aether Phase Power Solar Blood " \
                     "Sacred Guardian Silver Swift Arcane Vengeful Ancient Bounty".split()
        nouns = "Mage Spirit Back Knight Fiend Ranger Void Protector Destroyer Assassin Lancer Queen".split()
        verbs = "goes catches pushes splits pulls feeds".split()
        places = "mid bottom top fountain highground tormentor ancient roshpit".split()

        return f"{choice(adjectives)} {choice(nouns)} {choice(verbs)} {choice(places)}."
