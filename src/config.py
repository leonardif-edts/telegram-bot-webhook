from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    BOT_TOKEN: SecretStr
