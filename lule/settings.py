from starlette.config import Config
from envparse import env

env.read_envfile()

DB_URL = env("DB_URL", default="postgresql://localhost:5432/lule")
