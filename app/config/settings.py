from dotenv import load_dotenv
from os import environ

load_dotenv(".env")


class Settings:
    DOMAIN = environ.get("DOMAIN", "http://127.0.0.1")
    PORT = environ.get("PORT", 8000)
    BASE_URL = f"{DOMAIN}:{PORT}"


settings = Settings()