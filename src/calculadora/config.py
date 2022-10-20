from dynaconf import Dynaconf
from pathlib import Path

settings = Dynaconf(
  
    envvar_prefix="DYNACONF",
    root_path=Path(__file__).parent,
    settings_files=["settings.py", ".secrets.toml"],
    environment=True,
    load_dotenv=True,
)

ROOT_DIR = Path(__file__).parent


