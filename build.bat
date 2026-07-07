@echo off
echo === Build Parcheador Highway Blossoms ES v1.0 ===

REM Limpiar builds anteriores
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
del /q *.spec 2>nul

echo.
echo Compilando .exe...
python -m PyInstaller ^
    --onefile ^
    --windowed ^
    --name "HB_Parcheador_ES_v1.0" ^
    --add-data "parche;parche" ^
    --hidden-import tkinter ^
    --hidden-import tkinter.filedialog ^
    --hidden-import tkinter.messagebox ^
    --hidden-import tkinter.ttk ^
    parcheador.py

if exist "dist\HB_Parcheador_ES_v1.0.exe" (
    echo.
    echo === Build exitoso ===
    echo Ejecutable: dist\HB_Parcheador_ES_v1.0.exe
    dir "dist\HB_Parcheador_ES_v1.0.exe"
) else (
    echo.
    echo === Build fallido. Revisa los errores. ===
)

pause
