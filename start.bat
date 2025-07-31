@echo off
setlocal

echo 🚀 Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo 🐍 Rodando o script src\main.py...
python src\main.py

echo ✅ Execução finalizada.

:: Abre a pasta de Downloads
start "" "%USERPROFILE%\Downloads"

:: Fecha a janela do .bat automaticamente
exit
