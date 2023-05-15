SECRET_KEY = 'django-insecure-wvo8b$-^vr4c6k3(kxm48)w4)4ny(9%h(jg2)yn8wi9j2fco)k'
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
ALGORITHM = 'HS256'