import typing
import environ
from pathlib import Path
from dataclasses import dataclass, asdict

BASE_DIR: Path = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, False))

environ.Env.read_env(env_file=f"""{BASE_DIR / ".env"}""")


@dataclass(frozen=True)
class Config:
    BASE_DIR: Path = BASE_DIR
    APP_DIR: Path = BASE_DIR / "apps"
    EXCLUDE_DIRNAME: typing.Tuple[str] = ("__pycache__",)
    INSTALLED_APPS: typing.Tuple = (
        "apps.public",
        "apps.user",
    )

    @property
    def as_dict(self) -> typing.Dict:
        return asdict(self)
