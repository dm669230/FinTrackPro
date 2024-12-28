from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(override=True)

class IgnoredType:
    pass

class Settings(BaseSettings):
    model_config = SettingsConfigDict()
    app_name: str = "FinTrackPro"
    admin_email: str
    items_per_user: int = 50
    
    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int

    # Database setup
    DB_USER : str
    DB_PASSWORD : str
    SERVER_HOST : str
    SERVER_PORT : str
    DB_NAME : str


# To access the settings
settings = Settings()
print(settings.app_name)
print(settings.admin_email)
print(settings.DB_NAME)
print(settings.DB_PASSWORD)