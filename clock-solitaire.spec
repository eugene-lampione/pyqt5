# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['clock-solitaire.py'],
    pathex=[],
    binaries=[],
    datas=[('clock-solitaire.ui', '.'), ('csr.py', '.'), ('images', 'images')],
    hiddenimports=['PyQt5'],
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
    [],
    exclude_binaries=True,
    name='clock-solitaire',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='clock-solitaire',
)
app = BUNDLE(
    coll,
    name='clock-solitaire.app',
    icon=None,
    bundle_identifier=None,
)
