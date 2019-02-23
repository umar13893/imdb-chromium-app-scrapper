import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "web")

DATABASES = {
    'default': {
        # Database driver
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'USER': 'postgres',
        # 'NAME': 'eel_db',
        # 'PASSWORD': 'mypassword',
        # 'HOST': '127.0.0.1',
        # 'PORT': '5432',
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


INSTALLED_APPS = (
    'app_movies',
)

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = '6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa'

