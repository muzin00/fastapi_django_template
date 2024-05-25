from pathlib import Path

from . import envvars

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = envvars.DJANGO_DEBUG

# Application definition
INSTALLED_APPS = []

# Database
DATABASES = {
    "default": {
        "ENGINE": envvars.DB_ENGINE,
        "NAME": envvars.DB_DATABASE,
        "USER": envvars.DB_USER,
        "PASSWORD": envvars.DB_PASSWORD,
        "HOST": envvars.DB_HOST,
        "PORT": envvars.DB_PORT,
    }
}

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Tokyo"
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
