from pathlib import Path
from sanic import Blueprint
from config.config import Config

blueprint_list = set()

config = Config()

for path in Path(config.APP_DIR).iterdir():
    if path.is_dir() and path.name not in config.EXCLUDE_DIRNAME:
        module = __import__(f"apps.{path.name}.routes")
        if hasattr(module, path.name):
            app = getattr(module, path.name)
            blueprint_list.add(app.routes.blueprint)

blueprint = Blueprint.group(*blueprint_list, version_prefix="/api/v")
