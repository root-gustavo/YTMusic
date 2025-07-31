@echo off
setlocal
echo 🔍 Verificando se o winget está instalado...

where winget >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ winget já está instalado!
    goto :winget_ok
)

echo ⚠️  winget não foi encontrado. Tentando instalar...

:: Verifica se PowerShell está disponível
where powershell >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ PowerShell necessário para instalação do winget.
    pause
    exit /b
)

:: Baixa o instalador do App Installer da Microsoft Store (contém o winget)
powershell -Command "Start-Process 'ms-windows-store://pdp/?productid=9NBLGGH4NNS1'"

echo 📝 A Microsoft Store foi aberta para você instalar o App Installer.
echo ➕ Depois de instalar manualmente, rode este script novamente.
pause
exit /b

:winget_ok
echo 🧪 Testando winget...
winget --version

:: Instalar FFmpeg se necessário
echo 🛠 Instalando FFmpeg se necessário...
winget list ffmpeg | findstr /i "Gyan.FFmpeg" >nul
if %errorlevel% neq 0 (
    echo 📦 FFmpeg não encontrado. Instalando...
    winget install Gyan.FFmpeg.Essentials --accept-package-agreements --accept-source-agreements
) else (
    echo ✅ FFmpeg já está instalado.
)

:: Instalar Python se necessário
echo 🐍 Verificando se o Python está instalado...
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo 📦 Python não encontrado. Instalando...
    winget install --id Python.Python.3.13 --version 3.13.5 --silent --accept-package-agreements --accept-source-agreements
) else (
    echo ✅ Python já está instalado.
)

:: Executar installer.py
echo 🚀 Executando installer.py...
python installer.py

echo ✅ Ambiente pronto!
pause
endlocal
