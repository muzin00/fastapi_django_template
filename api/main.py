import os

import django
from fastapi import FastAPI

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.config.settings")
django.setup()


app = FastAPI()
