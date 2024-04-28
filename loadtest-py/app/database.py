from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
from os import getenv
from .schemas import RdsSecret, RdsSecretCreds

# Constants
DEFAULT_DB_PORT = 5432
DEFAULT_POOL_SIZE = 500

# ENV
db_url = getenv("DB_URL")
db_host = getenv("DB_HOST")
db_name = getenv("DB_NAME")
db_port = getenv("DB_PORT", DEFAULT_DB_PORT)
db_user = getenv("DB_USER")
db_password = getenv("DB_PASSWORD")
db_credentials = getenv("RDS_CREDENTIALS")
pool_size = int(getenv("POOL_SIZE", DEFAULT_POOL_SIZE))


if not db_url:
    if db_credentials:
        secret = RdsSecretCreds.parse_raw(db_credentials)
        db_user = secret.username
        db_password = secret.password

    db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


print("DB_URL: ", db_url)
print("POOL_SIZE: ", pool_size)

# Engine and session creation
engine = create_engine(db_url, pool_size=pool_size, max_overflow=10)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

print("DB Connected!")
