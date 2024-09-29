from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str
    USE_RANDOM_DELAY_IN_RUN: bool = True
    RANDOM_DELAY_IN_RUN: list[int] = [0, 15]
    COMPLETE_TASK: bool = True
    UPGRADE_FARM: bool = True
    UPGRADE_STORAGE: bool = True
    UPGRADE_POPULATION: bool = True
    UPGRADE_CARDS: bool = True
    MAX_UPGRADE_CARDS_PRICE: int = 20
    MINIMUM_BALANCE: int = -1
    SLEEP_TIME: int = 1800
    FAKE_USERAGENT: bool = True
    USE_REF_ID: bool = False
    REF_ID: str

    USE_PROXY_FROM_FILE: bool = True


settings = Settings()
