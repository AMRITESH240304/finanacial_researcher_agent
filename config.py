from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "My FastAPI Project"
    ENVIRONMENT: str = "development"
    MONGO_URI:str
    SERPER_API_KEY:str
    GROQ_API_KEY:str
    GEMINI_API_KEY:str

    class Config:
        env_file = ".env"

settings = Settings()
