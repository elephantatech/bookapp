"""settings.py"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """setting class to setup the key values"""
    database_username: str = "username"
    database_password: str = "password"
    database_host: str = "db"
    database_name: str = "dbname"

    class Config:
        """Assuming your .env file is in the same directory as your settings.py"""
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def sqlalchemy_database_uri(self) -> str:
        """Constructs the SQLAlchemy database URI from individual components."""
        return f"mysql+mysqlconnector://{self.database_username}:{self.database_password}@{self.database_host}/{self.database_name}"


settings = Settings()
