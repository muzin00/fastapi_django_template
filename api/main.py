import os

from django.conf import settings
from fastapi import FastAPI

# Load django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.config.settings")
settings.configure()


app = FastAPI()
