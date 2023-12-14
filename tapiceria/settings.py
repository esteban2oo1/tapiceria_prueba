from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-(itk3+@zqkh5%8_g=jr#lsk*v8mbas#0_i5u7@bx54dvqg$gw+'

DEBUG = False

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    'corsheaders',
    'users',
    'colores',
    'tiposTelas',
    'telas_colores',
    'tiposEspumillas',
    'tiposProductos',
    'tiposMateriales',
    'productos',
    'detallesTapizados',
    'detallesNoTapizados',
    'ventas',
    'ventasProductos',
    'compras',
    'comprasTelasColores',
    'comprasTiposEspumillas',
    'comprasTiposMateriales',
    'existenciasTelasColores',
    'existenciasEspumillas',
    'existenciasMateriales',
    'existenciasProductos',
    'pagos',
    'creditos',
    'abonos',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware', 
]

ROOT_URLCONF = 'tapiceria.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'tapiceria.wsgi.application'


DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'HOST': 'mjl1a0.stackhero-network.com',
    'OPTIONS': {
      'ssl_mode': 'REQUIRED',
    },
    'NAME': 'root',
    'USER': 'root',
    'PASSWORD': 'pY4Cpz3NCZvTsalpdafl5RzB3u7RhYMT'
  }
}

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tapiceria_m',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
"""

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL='users.User'


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL='/imagenes/'
STATIC_TMP = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT=os.path.join(BASE_DIR,'imagenes')

os.makedirs(STATIC_TMP, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True) 

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CORS_ALLOW_ALL_ORIGINS = True
                                  
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
}                       
