"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
#import os
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''
This gets the current files path (~/python_rest/config/base.py) 
and moves up three levels to ~/python_rest
created a variable that points to root of project 
and we can get any other file in the directory from it
'''
ROOT_DIR = environ.Path(__file__) -3
APPS_DIR = ROOT_DIR.path('project')

# when using docker containers, we'll read env vars from .env file
env = environ.Env()
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=False)
if READ_DOT_ENV_FILE:
    env_file = str(ROOT_DIR.path('.env'))
    print('Loading : {}'.format(env_file))
    env.read_env(env_file)
    print('The .env file has been loaded. See base.py for more information')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', False)

# Application definition
'''
Use tuples over lists because they are immutable
and the ease of concatenating them togther. ensures that
at runtime, project's installed apps can't be changed
'''
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'rest_framework',
)

LOCAL_APPS = (
    'project.api',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

'''
Same as node. Middleware takes requests/responses 
as they leave Django system and appies functions to them
before/after being processed (conveyor belt)
IMPORTANT: order matters. order dictates order of middleware processed
'''
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

'''
points to the URLconf module (a collection of URL guidelines)
that Django will handle requests/responses with
Django will look at that file to determine action
when user makes request to a page/resource
'''
ROOT_URLCONF = 'config.urls'

'''
List of settings applied to the template engines installed  
Probably won't need this with React frontend
'''
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

'''
aka Web Server Gateway Interface
Standard for python web frameworks that points to a server in the app 
this points to wsgi.py which Django will server when 
runserver command is executed
'''
WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  str(ROOT_DIR.path('db.sqlite3')),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

#where static files will be served at
STATIC_URL = '/static/'

# where collected static files will be placed
STATIC_ROOT = str(ROOT_DIR('staticfiles'))

#folders Django will look for static files in
STATICFILES_DIRS = (
    str(APPS_DIR.path('static')),
)

#Specifications on what files to look for
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

#URL appended to the root URL to server media data
MEDIA_URL = '/media/'

#where collected media files will be stored
MEDIA_ROOT = str(APPS_DIR('media'))

#rest framework configs
REST_FRAMEWORK = {
}