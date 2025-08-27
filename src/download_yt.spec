# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files, collect_all

# Coleta arquivos de dados do pyfiglet (fonts etc)
pyfiglet_datas = collect_data_files('pyfiglet')

# Coleta todos os arquivos necessários do yt_dlp (inclusive extratores e dependências dinâmicas)
yt_dlp_data, yt_dlp_binaries, yt_dlp_hiddenimports = collect_all('yt_dlp')

a = Analysis(
    ['download_yt\\__main__.py'],
    pathex=[],
    binaries=yt_dlp_binaries,
    datas=pyfiglet_datas + yt_dlp_data + [('../path.env', '.')],
    hiddenimports=yt_dlp_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='download_yt',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
