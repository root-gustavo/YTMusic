import os
import sys
from pathlib import Path
from dotenv import load_dotenv

if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(dotenv_path=BASE_DIR / "path.env")

# Pega a variável USER do .env (pode ter variáveis do sistema tipo %USERPROFILE%)
user_env = os.getenv("USER")

if user_env:
    # Expande variáveis do sistema (ex: %USERPROFILE%, $HOME)
    user_env_expanded = os.path.expandvars(user_env)
    USER = Path(user_env_expanded)
else:
    # Se não definido no .env, usa padrão: pasta Downloads do usuário atual
    USER = Path(os.getenv("USERPROFILE") or os.getenv("HOME") or "~").expanduser() / "Downloads"

# Garante que seja caminho absoluto, senão converte relativo para absoluto com base em BASE_DIR
if not USER.is_absolute():
    USER = (BASE_DIR / USER).resolve()
