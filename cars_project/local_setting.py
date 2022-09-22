# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8d4)jj@_zh60vo4^1uah^uwp9f8qp#mk_@f-=5pmpsw)rz$xuy'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'cars_database',
        'USER': 'root',
        'PASSWORD': 'qazwsx2022',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
