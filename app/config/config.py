from pydantic_settings import BaseSettings, SettingsConfigDict
import os
# import new_file
from dotenv import load_dotenv
load_dotenv()  # Make sure to load environment variables from the .env file



SECRET_KEY = "83daa0256a2289b0fb23693bf1f6034d44396675749244721a2b20e896e11662"

# Database setup
DB_USER = "postgres"
DB_PASSWORD = r"Vaibhav16@"
SERVER_HOST = "localhost"
SERVER_PORT = "5432"
DB_NAME = "postgres"

class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str
    items_per_user: int = 50
    model_config = SettingsConfigDict()
    # print(model_config.items())


# To access the settings
# settings = Settings()
# print(settings.app_name)
# print(settings.admin_email)