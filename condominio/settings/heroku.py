import environ

from condominio.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET_KEY")

#ALLOWED_HOSTS = env.list("calm-falls-92306.herokuapp.com")

ALLOWED_HOSTS = [".herokuapp.com", "calm-falls-92306"]

DATABASES = {
    "default": env.db(),
}