import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent.parent.resolve()
load_dotenv(dotenv_path=BASE_DIR / "path.env")

# Carrega variáveis do .env
user_env = os.getenv("USER")
data_file_env = os.getenv("DATA_FILE")
src_file_env = os.getenv("SRC_FILE")

# Verifica se as variáveis obrigatórias existem
if data_file_env is None or src_file_env is None:
    raise EnvironmentError("Variáveis DATA_FILE ou SRC_FILE não definidas no path.env")

# USER: se estiver vazio, usa a pasta Downloads do usuário
if not user_env:
    USER = Path(os.getenv("USERPROFILE")) / "Downloads"
else:
    USER = Path(user_env)
    if not USER.is_absolute():
        USER = BASE_DIR / USER

DATA_FILE = (BASE_DIR / data_file_env).resolve()
SRC_FILE = (BASE_DIR / src_file_env).resolve()
