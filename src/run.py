from src.api.api import baixar_audio_func
from config.path import USER
import pyfiglet
from colorama import init, Fore
import os
# import time

init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    limpar_tela()
    YOU = pyfiglet.figlet_format("YOU", font="banner3-D")
    tube = pyfiglet.figlet_format("   tube :", font="banner3-D")
    print(Fore.RED + YOU, Fore.WHITE + tube)

    print(Fore.YELLOW + "="*40)
    print(Fore.GREEN + "🎵 YouTube Music Downloader 🎵".center(40))
    print(Fore.YELLOW + "="*40)

    url = input(Fore.BLUE + "\n🔗 Digite a URL do vídeo do YouTube: ").strip()
    formato = input(Fore.BLUE + "🎧 Digite o formato para baixar (mp3 ou wav): ").strip().lower()

    try:
        resultado = baixar_audio_func(url, formato)
        print(Fore.GREEN + "\n✅ " + resultado["mensagem"])
        print(Fore.CYAN + f"✅ Arquivo: {resultado['arquivo']}")
        print(Fore.CYAN + f"💾 Salvo em: {USER}")
        input("Precione ENTER para fechar")

    except Exception as e:
        print(Fore.RED + f"\n❌ Erro: {e}")
        input("Precione ENTER para fechar")

if __name__ == "__main__":
    main()
