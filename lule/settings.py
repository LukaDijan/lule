from envparse import env

env.read_envfile()

DB_URL = env("DB_URL", default="postgresql://lule@localhost/lule")
