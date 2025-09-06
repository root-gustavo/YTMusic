# 🎵 YouTube Music Downloader v1.0.1

Baixe áudio de vídeos do YouTube de forma rápida e prática, com suporte a  formatos: (mp3 e wav).  

## ⚡ Para Usuários

1. Baixe diretamente do link: [YouTube Music Downloader](https://github.com/root-gustavo/YTMusic/releases/download/v1.0.1/YouTube.Music.Downloader.zip)
2. Se baixou o `YouTube.Music.Downloader.zip`, descompacte a pasta.
3. Execute o arquivo `Youtube Music Downloader.exe`.

---

## 🛠 Para Desenvolvedores

1. Instale Python **v3.13.6** ou versão compatível.
2. Crie uma virtual environment (venv) na raiz do projeto:
```bash
python -m venv venv
```
3. Ative a virtual environment (venv)
```bash
venv\Scripts\activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Para o projeto funcionar é preciso baixar o `FFmpeg.exe`
   - Baixe diretamente do meu release: [Download do FFmpeg](https://github.com/root-gustavo/YTMusic/releases/tag/ffmpeg)
   - Após baixar o `ffmpeg.zip` extraia a pasta
   > **Não** troque o nome da pasta extraida. Deixe como: `ffmpeg`
   - Mova a pasta para o local: `bin`
   - Então o caminho completo vai ficar: `bin/ffmpeg/ffmpeg.exe`

6. Gere o executável com PyInstaller:

```bash
pyinstaller download_yt.spec
```

> ✅ Ao final, a pasta `dist` conterá o arquivo `YouTube Music Downloader.exe` pronto para uso.

---

## 📋 Formatos de Áudio Suportados

| Formato | Observações                 |
| ------- | --------------------------- |
| MP3     | Qualidade padrão do YouTube |
| WAV     | Formato sem compressão      |

---

## 💻 Requisitos

* **Sistema Operacional:** Windows
* **Versão do programa:** v1.0.1
* **Tamanho do arquivo:** \~50 MB
* **Tamanho descompactado:** \~50,5 MB

---

## 🔄 Mudanças na v1.0.1

* **Atualização:** `ffmpeg.exe` embutido no executável principal
* **Correção:** Ajustes de caminhos e variáveis de ambiente para compatibilidade total com Windows

---

## ❗ Observações

* O programa requer internet para baixar vídeos.
* Pode mover o executável ou pasta descompactada para qualquer local do computador.
* Compatível apenas com Windows.