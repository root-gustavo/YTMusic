from pathlib import Path
import shutil
from config import USER, DATA_FILE

def move_archive():
    pasta = Path(DATA_FILE)
    arquivos = list(pasta.glob("*.*"))  # pega todos os arquivos na pasta
    
    if not arquivos:
        raise FileNotFoundError(f"Nenhum arquivo encontrado na pasta {pasta}")

    # pega o arquivo com data de modificação mais recente
    arquivo_mais_recente = max(arquivos, key=lambda f: f.stat().st_mtime)

    destino = Path(USER) / arquivo_mais_recente.name
    destino.parent.mkdir(parents=True, exist_ok=True)

    shutil.move(str(arquivo_mais_recente), str(destino))
    print(f"Arquivo movido para: {destino}")

if __name__ == "__main__":
    move_archive()
