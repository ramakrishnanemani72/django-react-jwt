# Django settings file

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.auth',
    'rest_framework',
    'rest_framework_simplejwt',
    'api',  # Your custom app
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
]

# Custom user model
AUTH_USER_MODEL = 'api.CustomUser'
