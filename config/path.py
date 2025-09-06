import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Caminho base: exe ou script Python
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys._MEIPASS)  # <- pasta temporária do PyInstaller
else:
    BASE_DIR = Path(__file__).resolve().parents[1]

# Carrega .env só no Python normal
env_path = BASE_DIR / "path.env"
if env_path.exists() and not getattr(sys, 'frozen', False):
    load_dotenv(dotenv_path=env_path)

# USER
user_env = os.getenv("USER")
USER = Path(os.path.expandvars(user_env)) if user_env else Path.home() / "Downloads"

# FFMPEG
ffmpeg_env = os.getenv("FFMPEG")
FFMPEG = Path(ffmpeg_env) / "ffmpeg.exe" if ffmpeg_env else BASE_DIR / "bin/ffmpeg/ffmpeg.exe"
