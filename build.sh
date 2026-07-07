#!/bin/bash
# Build del parcheador .exe para Windows
# Requiere: pip install pyinstaller
# Ejecutar en Windows o con wine

echo "=== Build Parcheador Highway Blossoms ES v1.0 ==="

# Limpiar
rm -rf build/ dist/ *.spec 2>/dev/null

# Build con PyInstaller (onefile, sin consola)
pyinstaller \
    --onefile \
    --windowed \
    --name "HB_Parcheador_ES_v1.0" \
    --add-data "parche/tl:parche/tl" \
    --add-data "parche/preferences.rpy:parche" \
    --add-data "parche/spanish_locale.rpy:parche" \
    --hidden-import tkinter \
    --hidden-import tkinter.filedialog \
    --hidden-import tkinter.messagebox \
    --hidden-import tkinter.ttk \
    parcheador.py

if [ -f "dist/HB_Parcheador_ES_v1.0.exe" ]; then
    echo ""
    echo "=== Build exitoso ==="
    echo "Ejecutable: dist/HB_Parcheador_ES_v1.0.exe"
    ls -lh dist/HB_Parcheador_ES_v1.0.exe
else
    echo ""
    echo "=== Build fallido. Revisa los errores. ==="
fi
