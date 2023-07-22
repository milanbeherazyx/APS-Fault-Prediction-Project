
from dataclasses import dataclass
import os
import pymongo
MONGO_DB_URL_ENV_KEY="MONGO_DB_URL"

@dataclass
class EnvironmentVariable:
    mongo_db_url:str=os.getenv(MONGO_DB_URL_ENV_KEY)


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)