import os
from pathlib import Path

from dotenv import dotenv_values
from sqlalchemy import URL


def read_boolean(value: str) -> bool:
    return value.lower() in ('true', 't', 'yes', 'y', 'on', '1')

DEBUG = read_boolean(str(os.environ.get('DEBUG', 'False')))

BASE_DIR = Path(__file__).resolve().parent.parent

if DEBUG:
    app_config = dotenv_values(BASE_DIR / 'instance' / '.env.dev')
else:
    app_config = dotenv_values(BASE_DIR / 'instance' / '.env')

SECRET_KEY = app_config['SECRET_KEY']

DATABASE_URL = URL.create(
        'postgresql',
        username=app_config['POSTGRES_USER'],
        password=app_config['POSTGRES_PASSWORD'],  # plain (unescaped) text
        host=app_config.get('POSTGRES_HOST', 'postgres'),
        port=app_config.get('POSTGRES_PORT', '5432'),
        database=app_config.get('POSTGRES_DB', 'postgres'),
        query={'options': f'-c search_path={app_config.get("POSTGRES_SCHEMA", "public")}'},
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
