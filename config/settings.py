import os
import shutil
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-change-this-secret-key-lapak-warga")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = [
    "*",
    "localhost",
    "127.0.0.1",
    ".vercel.app",
]
env_hosts = os.getenv("ALLOWED_HOSTS")
if env_hosts:
    ALLOWED_HOSTS.extend([h.strip() for h in env_hosts.split(",") if h.strip()])

CSRF_TRUSTED_ORIGINS = [
    "https://*.vercel.app",
    "https://*.now.sh",
    "https://lapak-warga-roan.vercel.app",
    "http://127.0.0.1",
    "http://localhost",
]
env_csrf = os.getenv("CSRF_TRUSTED_ORIGINS")
if env_csrf:
    CSRF_TRUSTED_ORIGINS.extend([c.strip() for c in env_csrf.split(",") if c.strip()])

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "marketplace",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "templates"],
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.debug",
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ]},
}]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

# Database Configuration
db_url = os.getenv("DATABASE_URL", "").strip()

if db_url:
    DATABASES = {
        "default": dj_database_url.parse(
            db_url,
            conn_max_age=0,
        )
    }

    DATABASES["default"]["OPTIONS"] = {
        **DATABASES["default"].get("OPTIONS", {}),
        "charset": "utf8mb4",
        "ssl": {
            "check_hostname": True,
        },
    }

elif os.getenv("VERCEL"):
    raise RuntimeError(
        "DATABASE_URL belum dikonfigurasi di Vercel."
    )

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
    
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "id"
TIME_ZONE = "Asia/Makassar"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
WHITENOISE_USE_FINDERS = True

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "home"