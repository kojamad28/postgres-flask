from dotenv import dotenv_values
from sqlalchemy import URL

app_config = dotenv_values('instance/.env.dev')
#app_config = dotenv_values('instance/.env')

DEBUG = app_config.get('DEBUG', 'false').lower() == 'true'

SECRET_KEY = app_config['SECRET_KEY']

DATABASE_URL = URL.create(
        'postgresql',
        username=app_config['DATABASE_USER'],
        password=app_config['DATABASE_PASSWORD'],  # plain (unescaped) text
        host=app_config.get('DATABASE_HOST', 'postgres'),
        port=app_config.get('DATABASE_PORT', '5432'),
        database=app_config.get('DATABASE_DB', 'postgres'),
        query={'options': f'-c search_path={app_config.get("DATABASE_SCHEMA", "public")}'},
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
