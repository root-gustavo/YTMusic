import subprocess
import sys
import venv
from pathlib import Path

# Caminhos
base_dir = Path(__file__).parent.resolve()
venv_dir = base_dir / "venv"
requirements_file = base_dir / "requirements.txt"

# 1. Criar a venv se não existir
if not venv_dir.exists():
    print("🔧 Criando ambiente virtual...")
    venv.create(venv_dir, with_pip=True)
else:
    print("✅ Ambiente virtual já existe.")

# 2. Caminho para o pip dentro da venv
if sys.platform == "win32":
    pip_path = venv_dir / "Scripts" / "pip.exe"
else:
    pip_path = venv_dir / "bin" / "pip"

# 3. Instalar os requirements.txt
if requirements_file.exists():
    print(f"📦 Instalando pacotes de {requirements_file.name}...")
    subprocess.check_call([str(pip_path), "install", "-r", str(requirements_file)])
    print("✅ Pacotes instalados com sucesso.")
else:
    print("⚠️ Nenhum arquivo requirements.txt encontrado.")
