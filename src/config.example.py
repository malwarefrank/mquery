from typing import List

INDEX_DIR = "./samples"
BACKEND = "tcp://127.0.0.1:9281"
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
JOB_EXPIRATION_MINUTES = 0  # infinite by default
PLUGINS: List[str] = []
