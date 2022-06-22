import redis

class RedisConnection:

    @classmethod
    def getConnection(cls):
        # creating a connection to local redis server
        redis_cli = redis.Redis(host="localhost", port=16379, decode_responses=True, encoding="utf-8")
        return redis_cli
    
    @classmethod
    def getPubSubClient(cls):
        connection = cls.getConnection()
        # creating a pubsub client
        pubsub_client = connection.pubsub()
        msg = pubsub_client.get_message()
        return pubsub_client
