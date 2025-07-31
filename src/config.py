import os
from pathlib import Path
from dotenv import load_dotenv

# Carregue o seu arquivo .env customizado
load_dotenv(dotenv_path=Path(__file__).parent.parent / "path.env")

BASE_DIR = Path(__file__).parent.resolve()

user_env = os.getenv("USER")
data_file_env = os.getenv("DATA_FILE")
src_file_env = os.getenv("SRC_FILE")

if user_env is None or data_file_env is None or src_file_env is None:
    raise EnvironmentError("Variáveis USER, DATA_FILE ou SRC_FILE não definidas no path.env")

USER = Path(user_env)
DATA_FILE = Path(data_file_env)
SRC_FILE = Path(src_file_env)
