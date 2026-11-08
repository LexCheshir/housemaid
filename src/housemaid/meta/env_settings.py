import importlib

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field(description="App name. Used for version resolution.")
    debug: bool = Field(
        description="Dev environment flag",
        default=False,
    )
    discord_app_id: str = ""
    discord_public_key: str = ""
    discord_token: str = Field(
        description="Discord bot token. Used for Discord client authentication.",
        default="",
    )

    @computed_field
    @property
    def version(self) -> str:
        return importlib.metadata.version(self.app_name)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="housemaid_",
        env_file_encoding="utf-8",
    )
