from config import DATA_FILE
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yt_dlp
import subprocess
import os
import uuid
import platform

app = FastAPI()

AUDIO_DIR = DATA_FILE
os.makedirs(AUDIO_DIR, exist_ok=True)

class AudioRequest(BaseModel):
    url: str
    formato: str  # "mp3" ou "wav"

def get_ffmpeg_cmd():
    return "ffmpeg.exe" if platform.system() == "Windows" else "ffmpeg"

import re

def sanitize_filename(name: str) -> str:
    # Remove caracteres inválidos para nomes de arquivos no Windows
    return re.sub(r'[\\/*?:"<>|]', "", name)

def baixar_audio_func(url: str, formato: str) -> dict:
    if formato not in ["mp3", "wav"]:
        raise ValueError("Formato inválido. Use 'mp3' ou 'wav'.")

    opcoes = {
        'format': 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        info = ydl.extract_info(url, download=False)  # só extrair info
        titulo = sanitize_filename(info.get('title', 'audio'))

    nome_base = titulo
    os.makedirs(AUDIO_DIR, exist_ok=True)
    saida_padrao = os.path.join(AUDIO_DIR, f"{nome_base}.%(ext)s")
    caminho_final = os.path.join(AUDIO_DIR, f"{nome_base}.{formato}")

    opcoes['outtmpl'] = saida_padrao

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        info = ydl.extract_info(url, download=True)
        arquivo_baixado = ydl.prepare_filename(info)

    if not arquivo_baixado.endswith(formato):
        subprocess.run([
            get_ffmpeg_cmd(),
            '-y',
            '-i', arquivo_baixado,
            caminho_final
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.remove(arquivo_baixado)
    else:
        caminho_final = arquivo_baixado

    return {
        "mensagem": "Áudio baixado com sucesso!",
        "arquivo": os.path.basename(caminho_final)
    }


@app.post("/baixar-audio/")
def baixar_audio(req: AudioRequest):
    try:
        return baixar_audio_func(req.url, req.formato)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
