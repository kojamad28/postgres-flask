from dotenv import dotenv_values
from sqlalchemy import URL

app_config = dotenv_values('instance/.env.dev')
#app_config = dotenv_values('instance/.env')

DEBUG = app_config.get('DEBUG', 'false').lower() == 'true'

SECRET_KEY = app_config['SECRET_KEY']

SQLALCHEMY_DATABASE_URI = URL.create(
        'postgresql+psycopg',
        username=app_config['DATABASE_USER'],
        password=app_config['DATABASE_PASSWORD'],  # plain (unescaped) text
        host=app_config['DATABASE_HOST'],
        port=app_config['DATABASE_PORT'],
        database=app_config['DATABASE_DB'],
        query={'options': f'-c search_path={app_config["DATABASE_SCHEMA"]}'},
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
