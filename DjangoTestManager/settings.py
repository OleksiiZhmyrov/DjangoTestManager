"""
Django settings for DjangoTestManager project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
from DjangoTestManager.settings_local import SECRET_KEY as SECRET_KEY_LOCAL

SECRET_KEY = SECRET_KEY_LOCAL

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'TestManagerCore',
    'TestManagerContent',
    'TestManagerExec',
    'axes',
    'django_summernote',
    'django_bleach',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'TestManagerCore.middleware.SessionExpiry',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'TestManagerCore.middleware.PageGenerationDatetime',
    'TestManagerCore.middleware.UserprofileContextInjector',
    'axes.middleware.FailedLoginMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.contrib.auth.context_processors.auth',
)

ROOT_URLCONF = 'DjangoTestManager.urls'

WSGI_APPLICATION = 'DjangoTestManager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'templates/static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'init/fixtures/'),
)

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_EXPIRY = 1800

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'app_cache',
    }
}

LOGIN_REDIRECT_URL = '/'

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

CONTENT_TYPES = ['image/jpeg', 'image/png', ]
MAX_UPLOAD_SIZE = 2621440

MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'

from DjangoTestManager.settings_local import JIRA_BROWSE_URL as JIRA_BROWSE_URL_LOCAL

JIRA_BROWSE_URL = JIRA_BROWSE_URL_LOCAL

AXES_LOCKOUT_TEMPLATE = "pages/account_locked.html"
AXES_COOLOFF_TIME = 24

SUMMERNOTE_CONFIG = {
    'iframe': True,
    'airMode': False,
    'styleWithTags': True,
    'direction': 'ltr',
    'width': '100%',
    'height': '320',
    'toolbar': [
        ['style', ['style']],
        ['misc', ['undo', 'redo']],
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['para', ['ul', 'ol']],
        ['misc', ['codeview']],
        ['misc', ['help']]
    ],
}

BLEACH_ALLOWED_TAGS = [
    'p',
    'b', 'i', 'u',
    'ul', 'ol', 'li',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'span', 'pre', 'blockquote',
]

BLEACH_ALLOWED_ATTRIBUTES = [
    'style',
]

BLEACH_ALLOWED_STYLES = [
    'font-family',
    'font-weight',
    'text-decoration',
    'font-variant',
    'color',
]

BLEACH_STRIP_TAGS = True

BLEACH_STRIP_COMMENTS = True

LOG_FILENAME = './env/log.txt'

PIE_CHART_OPTIONS = {
    'segmentShowStroke': 'true',
    'segmentStrokeColor': "#FFFFFF",
    'segmentStrokeWidth': 2,
}