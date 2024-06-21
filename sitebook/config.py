from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    secret_key: str
    smtp_key: str
    email_host_user: str
    email_host: str
    model_config = SettingsConfigDict(env_file=".env")


envs = Settings()  # type: ignore
