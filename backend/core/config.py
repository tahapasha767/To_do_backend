from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Mini Tasks API"
    DEBUG: bool = True


settings = Settings()
