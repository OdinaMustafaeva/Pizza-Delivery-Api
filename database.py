from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

env = dotenv_values(".env")

DB_NAME = env.get("DB_NAME")
DB_USER = env.get("DB_USER")
DB_PASSWORD = env.get("DB_PASSWORD")
SQL_ALCHEMY_DB_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}'
engine = create_engine(SQL_ALCHEMY_DB_URL, echo=True)

Base = declarative_base()

Session = sessionmaker()
