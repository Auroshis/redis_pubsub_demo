from redis_handler import RedisConnection

class Publisher:

    def __init__(self, channel) -> None:
        self.channel = channel
        self.redis_con = RedisConnection.getConnection()

    def createChannel(self):
        """Method to create an channel"""
        self.redis_con.publish(channel=self.channel,message="hello world!")
        return True
    
    def publishMessage(self, msg):
        """Method to publish a Message"""
        readers = self.redis_con.publish(channel=self.channel, message=msg)
        return readers
