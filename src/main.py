from functions.move_download import move_archive
from apis.api import *
import time
import subprocess

def main():
    print("=== YouTube Music Downloader ===")
    url = input("Digite a URL do vídeo do YouTube: ").strip()
    formato = input("Digite o formato para baixar (mp3 ou wav): ").strip().lower()

    try:
        resultado = baixar_audio_func(url, formato)
        print("\n" + resultado["mensagem"])
        print(f"Arquivo salvo: {resultado['arquivo']}")
    except Exception as e:
        print(f"Erro: {e}")

    time.sleep(1)

    move_archive()

if __name__ == "__main__":
    main()
