from redis_handler import RedisConnection
import time

class Subscriber:

    def __init__(self, name) -> None:
        self.name = name
        self.ps_cli = RedisConnection.getPubSubClient()

    def addSubscription(self, channel):
        # getting pubsub client 
        # check if channel exists or not - to do 
        self.ps_cli.subscribe(channel)
        # for simplicity we are not going into exception handling and logging
        return True
    
    def getNewMessages(self):
        
        while True:
            msg = self.ps_cli.get_message()
            try:
                if msg['type'] == 'message':
                    print("""Channel - {0}\n{1}\n""".format(msg['channel'], msg['data']))
            except TypeError:
                continue
            # to conveniently show the messages without vanishing quickly
            time.sleep(15)