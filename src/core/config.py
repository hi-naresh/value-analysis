from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Reflection Journal Entry Analysis API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    MODEL_NAME: str = "facebook/bart-large-mnli"
    THRESHOLD: float = 20.0


settings = Settings()
