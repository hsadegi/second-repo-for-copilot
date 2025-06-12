# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['Run.py'],
    pathex=[r"C:\Users\amirreza\AppData\Local\Programs\Python\Python37\Lib\site-packages",r"C:\Users\amirreza\AppData\Local\Programs\Python\Python37\Libs"],
    binaries=[],
    datas=[('Source\\Images\\Lung_Icon.ico', '.\\Source\\Images\\Lung_Icon.ico'), ('Plugins_Manager', '.\\Plugins_Manager')],
    hiddenimports=['sklearn.utils._cython_blas', 'sklearn.metrics._pairwise_distances_reduction', 'ipykernel.datapub','pkg_resources.py2_warn'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='MedVisPy37',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=r'E:\\python_venv\\medvispy\\Source\\Images\\Lung_Icon.ico',
)
OPTIONS = ['-w', '--hidden-import tensorflow']
