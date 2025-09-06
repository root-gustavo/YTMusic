# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.building.build_main import Analysis, PYZ, EXE

a = Analysis(
    ['src/__main__.py'],
    pathex=['.'],  # garante que a pasta raiz do projeto está no sys.path
    binaries=[],
    datas=[
        ('config', 'config'),
        ('path.env', '.'),
        ('bin', 'bin'),
        ('venv/Lib/site-packages/pyfiglet/fonts', 'pyfiglet/fonts'),
    ],
    hiddenimports=[],
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
    name='YouTube Music Downloader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    icon="icon/youtube.ico",
)
