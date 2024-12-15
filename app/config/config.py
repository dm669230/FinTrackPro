from pydantic_settings import BaseSettings, SettingsConfigDict
import os
# import new_file
from dotenv import load_dotenv
load_dotenv()  # Make sure to load environment variables from the .env file


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "487daba42d2cacb9442ee2a6670782d0026cf21dd3c4d78a91ba1a1ec5118edd"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Database setup
DB_USER = "postgres"
DB_PASSWORD = r"Vaibhav16@"
SERVER_HOST = "localhost"
SERVER_PORT = "5432"
DB_NAME = "postgres"

class Settings(BaseSettings):
    app_name: str = "FinTrackPro"
    admin_email: str
    items_per_user: int = 50
    model_config = SettingsConfigDict()
    # print(model_config.items())


# To access the settings
# settings = Settings()
# print(settings.app_name)
# print(settings.admin_email)