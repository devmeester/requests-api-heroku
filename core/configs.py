from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:9a0860B6@hardwaredb.cvezjiq03s8a.sa-east-1.rds.amazonaws.com:5432/hardwaredb'

    class Config:
        case_sensitive = True


settings: Settings = Settings()