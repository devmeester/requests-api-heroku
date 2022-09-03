from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:bm1U7Qe6tBWqCOcmj4If@hardwaredb.czbomnjyhr9g.us-east-1.rds.amazonaws.com:5432/hardwaredb'

    class Config:
        case_sensitive = True


settings: Settings = Settings()
