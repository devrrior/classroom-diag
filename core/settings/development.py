import environ

from .base import *

env = environ.Env()

environ.Env.read_env("development.env")

SECRET_KEY = 'django-insecure-&oh(q-oq0nvy&n^tsgr)dlfsw%s6hbs0$_wa2auudtqx^l=yh-'
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": env("DATABASE_HOST"),
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "PORT": env("DATABASE_PORT"),
    }
}