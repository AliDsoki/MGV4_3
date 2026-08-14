# -*- mode: python ; coding: utf-8 -*-
# ملف بناء PyInstaller لبرنامج MG Downloader v4.3
#
# للبناء يدويًا (على ويندوز):
#     pyinstaller MGV4_3.spec
#
# الناتج يظهر في مجلد dist/ باسم "MG Downloader v4.3.exe"

import os

block_cipher = None

# أيقونة البرنامج: يجب أن يكون ملف mg.ico موجودًا في جذر المستودع بجانب هذا الملف.
# لو لم يكن موجودًا، يبني PyInstaller البرنامج بدون أيقونة مخصّصة بدل أن يفشل البناء.
ICON_PATH = "mg.ico" if os.path.exists("mg.ico") else None

# نُضمّن الأيقونة كملف بيانات داخل الحزمة أيضًا، لأن الكود نفسه (find_app_icon_path)
# يبحث عنها في مجلد sys._MEIPASS وقت التشغيل لعرضها في شريط المهام وعنوان النافذة.
datas = []
if ICON_PATH:
    datas.append((ICON_PATH, "."))

a = Analysis(
    ["MGV4_3.py"],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
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
    name="MG Downloader v4.3",
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
    icon=ICON_PATH,
)
