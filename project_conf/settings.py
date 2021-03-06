import os
from django.core.urlresolvers import reverse_lazy

CONF_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CONF_DIR)
PROJECT_NAME = "TestTiffin"
CONF_DIR_NAME = os.path.relpath(CONF_DIR,BASE_DIR)

LOGIN_URL = reverse_lazy("accounts:login")
LOGOUT_URL = reverse_lazy("accounts:logout")
LOGIN_REDIRECT_URL = reverse_lazy("main:index")
LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# secret_key.txt is not versioned controlled (for use in production)
# old_secret_key.txt is versioned controlled
try:
	with open(os.path.join(CONF_DIR,"secret","secret_key.txt")) as _secret_key_file:
		SECRET_KEY = _secret_key_file.read().strip()
except FileNotFoundError:
	with open(os.path.join(CONF_DIR,"old_secret_key.txt")) as _secret_key_file:
		SECRET_KEY = _secret_key_file.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'main',
	'accounts',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = CONF_DIR_NAME+'.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR,"templates")],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'main.context_processors.settings_processor'
			],
		},
	},
]

WSGI_APPLICATION = CONF_DIR_NAME+'.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

import json
DATABASES = {}
db_paths = [
	os.path.join(CONF_DIR,"secret","postgresql.json"),
	os.path.join(CONF_DIR,"secret","mysql.json"),
]
_db_file_found = False

for _db_path in db_paths:
	if not _db_file_found:
		try:
			with open(_db_path) as _db_setting_file:
				DATABASES["default"] = json.load(_db_setting_file)
				_db_file_found = True
		except (FileNotFoundError, ValueError):
			pass

if not _db_file_found:
	DATABASES["default"] = {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'sqlite3.db'),
	}
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'mydatabase',
#        'USER': 'mydatabaseuser',
#        'PASSWORD': 'mypassword',
#        'HOST': 'localhost',
#        'PORT': '',
#    }
#}



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
EXTSTATIC_DIR = os.path.join(BASE_DIR,'extstatic')
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'), EXTSTATIC_DIR)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Link to external CSS and JS libraries

LIB_URLS_WEB = {
	"jquery": 'https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js',
	"bootstrap_css": 'https://maxcdn.bootstrapcdn.com/bootstrap/latest/css/bootstrap.min.css',
	"bootstrap_js": 'https://maxcdn.bootstrapcdn.com/bootstrap/latest/js/bootstrap.min.js',
	"mathjax": 'https://cdn.mathjax.org/mathjax/latest/MathJax.js',
}

LIB_URLS_LOCAL_SUFFIX = {
	"jquery": 'jquery.min.js',
	"bootstrap_css": 'bootstrap/css/bootstrap.css',
	"bootstrap_js": 'bootstrap/js/bootstrap.js',
	"mathjax": 'mathjax/MathJax.js',
}

LIB_URLS = {}

for libname,fname in LIB_URLS_LOCAL_SUFFIX.items():
	try:
		_libfile = open(os.path.join(EXTSTATIC_DIR,fname))
		_libfile.close()
		LIB_URLS[libname] = STATIC_URL + fname
	except FileNotFoundError:
		LIB_URLS[libname] = LIB_URLS_WEB[libname]
	if DEBUG:
		print("{libname}:\t{liburl}".format(libname=libname,liburl=LIB_URLS[libname]))
