from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "My FastAPI Project"
    ENVIRONMENT: str = "development"
    HOST: str
    PORT: int
    MONGO_URI:str
    GOOGLE_SEARCH_KEY:str
    SEARCH_ENGINE_ID:str
    EXA_API_KEY:str
    SERPER_API_KEY:str
    GROQ_API_KEY:str
    GEMINI_API_KEY:str
    awscli_secret_key: str
    awscli_access_key: str
    alpha_vantage_key: str

    class Config:
        env_file = ".env"

settings = Settings()
