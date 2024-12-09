import redis


REDIS_HOST = "localhost"
REDIS_PORT = 6379
SESSION_EXPIRATION = 3600

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
