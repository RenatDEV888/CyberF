# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/vor13/PycharmProjects/darkbaseprobiv/main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/vor13/PycharmProjects/darkbaseprobiv/bases/AlfaBank1.xlsx', '.'), ('C:/Users/vor13/PycharmProjects/darkbaseprobiv/bases/ForaBankMoscow.xlsx', '.'), ('C:/Users/vor13/PycharmProjects/darkbaseprobiv/bases/IpOZON1.xlsx', '.'), ('C:/Users/vor13/PycharmProjects/darkbaseprobiv/bases/MAX.xlsx', '.'), ('C:/Users/vor13/PycharmProjects/darkbaseprobiv/bases/OZON2.xlsx', '.'), ('C:/Users/vor13/PycharmProjects/darkbaseprobiv/bases/PromBank1.xlsx', '.'), ('C:/Users/vor13/PycharmProjects/darkbaseprobiv/bases/RaifFazenBank.xlsx', '.'), ('C:/Users/vor13/PycharmProjects/darkbaseprobiv/bases/RenesansBank.xlsx', '.'), ('C:/Users/vor13/PycharmProjects/darkbaseprobiv/bases/RFdate1.xlsx', '.'), ('C:/Users/vor13/PycharmProjects/darkbaseprobiv/bases/RosBank1.xlsx', '.'), ('C:/Users/vor13/PycharmProjects/darkbaseprobiv/bases/RosselhozBank.xlsx', '.'), ('C:/Users/vor13/PycharmProjects/darkbaseprobiv/bases/Tinkoff1.xlsx', '.'), ('C:/Users/vor13/PycharmProjects/darkbaseprobiv/bases/YandexSPB1.xlsx', '.'), ('C:/Users/vor13/PycharmProjects/darkbaseprobiv/bases/*', '.')],
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
    name='Cyber F',
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
    icon=['C:\\Users\\vor13\\PycharmProjects\\darkbaseprobiv\\icon.ico'],
)
