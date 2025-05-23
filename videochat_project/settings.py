import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INSTALLED_APPS = [ 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'call',
]

CHANNEL_LAYERS = {
    "default":{
        "BACKEND": "channels_redis.core.RedisChannelLayer",
	 "CONFIG": {

	  "hosts":[{"127.0.0.1", 6379}]


}


}

}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # This tells Django to use SQLite
        'NAME': BASE_DIR / 'db.sqlite3',         # Path to the SQLite database file
    }
}

SECRET_KEY = 'H$Pr()je(t$2025'
ROOT_URLCONF = 'videochat_project.urls'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Required
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required
    'django.contrib.messages.middleware.MessageMiddleware',  # Required
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # or add your custom template paths here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [
	BASE_DIR / "STATIC",
]
STATIC_ROOT = BASE_DIR / "staticfiles"
ASGI_APPLICATION = "videochat_project.asgi.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    },
}
DEBUG = True
ALLOWED_HOSTS = ['*']
