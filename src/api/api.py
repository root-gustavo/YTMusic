from config.path import USER, FFMPEG
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yt_dlp
import subprocess
import os
import re
from pathlib import Path
# import sys
# import platform

app = FastAPI()

AUDIO_DIR = USER
os.makedirs(AUDIO_DIR, exist_ok=True)
print(f"[API] Pasta de áudio: {AUDIO_DIR}")

class AudioRequest(BaseModel):
    url: str
    formato: str  # "mp3" ou "wav"

def get_ffmpeg_cmd():
    return str(FFMPEG)

def sanitize_filename(name: str) -> str:
    return re.sub(r'[\\/*?:"<>|]', "", name)

def baixar_audio_func(url: str, formato: str) -> dict:
    print(f"[API] Iniciando download: {url} como {formato}")
    if formato not in ["mp3", "wav"]:
        raise ValueError("Formato inválido. Use 'mp3' ou 'wav'.")

    opcoes = {
        'format': 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        info = ydl.extract_info(url, download=False)
        titulo = sanitize_filename(info.get('title', 'audio'))
        print(f"[API] Título do vídeo: {titulo}")

    nome_base = titulo
    saida_padrao = os.path.join(AUDIO_DIR, f"{nome_base}.%(ext)s")
    caminho_final = os.path.join(AUDIO_DIR, f"{nome_base}.{formato}")
    opcoes['outtmpl'] = saida_padrao

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        info = ydl.extract_info(url, download=True)
        arquivo_baixado = ydl.prepare_filename(info)
        print(f"[API] Arquivo baixado: {arquivo_baixado}")

    if not arquivo_baixado.endswith(formato):
        ffmpeg_cmd = get_ffmpeg_cmd()
        if not Path(ffmpeg_cmd).exists():
            raise FileNotFoundError(f"FFmpeg não encontrado: {ffmpeg_cmd}")
        
        print(f"[API] Convertendo com ffmpeg para: {formato}")
        subprocess.run([
            ffmpeg_cmd,
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
        print(f"[ERRO] Valor inválido: {ve}")
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        print(f"[ERRO] Exceção inesperada: {e}")
        raise HTTPException(status_code=500, detail=str(e))
