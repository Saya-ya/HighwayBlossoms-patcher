#!/usr/bin/env python3
"""
Highway Blossoms - Parcheador de Traduccion al Espanol v1.0
Aplica la traduccion al espanol a una instalacion existente del juego.
Compatible con Highway Blossoms 1.3.1 - Unified.
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import sys
import shutil
from pathlib import Path

VERSION = "1.0"
GAME_VERSION = "1.3.1 - Unified"
PARCHE_DIR = Path(__file__).parent / "parche"


class ParcheadorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(f"Highway Blossoms - Parcheador Espanol v{VERSION}")
        self.root.geometry("580x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#2b2725")
        
        try:
            icon = tk.PhotoImage(file=str(PARCHE_DIR / "icon.png"))
            self.root.iconphoto(True, icon)
        except:
            pass
        
        self.game_path = tk.StringVar()
        self.status_text = tk.StringVar(value="Listo. Selecciona la carpeta del juego.")
        self.progress_var = tk.DoubleVar()
        
        self._build_ui()
    
    def _build_ui(self):
        # Header
        header = tk.Frame(self.root, bg="#ff7152", height=80)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        tk.Label(
            header, 
            text=f"Highway Blossoms\nParcheador de Traduccion al Espanol v{VERSION}",
            font=("Segoe UI", 16, "bold"),
            fg="white",
            bg="#ff7152",
            justify="center"
        ).pack(expand=True)
        
        # Body
        body = tk.Frame(self.root, bg="#2b2725", padx=30, pady=20)
        body.pack(fill="both", expand=True)
        
        # Compatible version info
        info_frame = tk.Frame(body, bg="#3a3532", padx=15, pady=10)
        info_frame.pack(fill="x", pady=(0, 20))
        
        tk.Label(
            info_frame,
            text=f"Version compatible: Highway Blossoms {GAME_VERSION}",
            font=("Segoe UI", 11),
            fg="#f6f2e4",
            bg="#3a3532"
        ).pack(anchor="w")
        
        tk.Label(
            info_frame,
            text="Idiomas disponibles: Ingles, Chino, Frances, Ruso, Espanol",
            font=("Segoe UI", 9),
            fg="#888",
            bg="#3a3532"
        ).pack(anchor="w")
        
        # Game folder selection
        select_frame = tk.Frame(body, bg="#2b2725")
        select_frame.pack(fill="x", pady=(0, 10))
        
        tk.Label(
            select_frame,
            text="Carpeta del juego:",
            font=("Segoe UI", 10, "bold"),
            fg="#f6f2e4",
            bg="#2b2725"
        ).pack(anchor="w")
        
        path_frame = tk.Frame(select_frame, bg="#2b2725")
        path_frame.pack(fill="x", pady=(5, 0))
        
        self.path_entry = tk.Entry(
            path_frame,
            textvariable=self.game_path,
            font=("Segoe UI", 9),
            bg="#3a3532",
            fg="#f6f2e4",
            insertbackground="#f6f2e4",
            relief="flat",
            state="readonly",
            readonlybackground="#3a3532"
        )
        self.path_entry.pack(side="left", fill="x", expand=True, ipady=6)
        
        tk.Button(
            path_frame,
            text="Examinar...",
            command=self._browse_folder,
            bg="#ff7152",
            fg="white",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            padx=15,
            pady=6,
            cursor="hand2",
            activebackground="#e05a3a"
        ).pack(side="left", padx=(8, 0))
        
        # Action buttons
        btn_frame = tk.Frame(body, bg="#2b2725")
        btn_frame.pack(fill="x", pady=(10, 5))
        
        self.patch_btn = tk.Button(
            btn_frame,
            text="Aplicar Parche",
            command=self._apply_patch,
            bg="#ff7152",
            fg="white",
            font=("Segoe UI", 12, "bold"),
            relief="flat",
            padx=30,
            pady=10,
            cursor="hand2",
            activebackground="#e05a3a",
            state="disabled"
        )
        self.patch_btn.pack(fill="x")
        
        # Progress bar
        self.progress = ttk.Progressbar(
            body,
            variable=self.progress_var,
            mode="indeterminate",
            length=200
        )
        self.progress.pack(fill="x", pady=(10, 5))
        
        # Status
        status_frame = tk.Frame(body, bg="#2b2725")
        status_frame.pack(fill="x")
        
        self.status_label = tk.Label(
            status_frame,
            textvariable=self.status_text,
            font=("Segoe UI", 9),
            fg="#888",
            bg="#2b2725",
            wraplength=500,
            justify="center"
        )
        self.status_label.pack()
        
        # Footer
        footer = tk.Frame(self.root, bg="#1a1817", height=30)
        footer.pack(fill="x", side="bottom")
        tk.Label(
            footer,
            text="Traduccion por fans. Highway Blossoms (c) Studio Elan.",
            font=("Segoe UI", 8),
            fg="#555",
            bg="#1a1817"
        ).pack(expand=True)
    
    def _browse_folder(self):
        folder = filedialog.askdirectory(title="Selecciona la carpeta del juego")
        if folder:
            self.game_path.set(folder)
            self._validate_path()
    
    def _validate_path(self):
        path = Path(self.game_path.get())
        
        if not path.exists():
            self.status_text.set("La carpeta no existe.")
            self.patch_btn.configure(state="disabled")
            return
        
        # Check for game files
        exe = path / "HighwayBlossoms.exe"
        exe_alt = path / "HighwayBlossoms.sh"
        game_dir = path / "game"
        
        if exe.exists() or exe_alt.exists():
            self.status_text.set("Juego detectado. Listo para parchear.")
            self.patch_btn.configure(state="normal")
        elif game_dir.exists():
            self.status_text.set("Carpeta 'game/' detectada (podria ser el subdirectorio).")
            self.patch_btn.configure(state="normal")
        else:
            self.status_text.set("ERROR: No se encontro HighwayBlossoms.exe/.sh. Selecciona la carpeta raiz del juego.")
            self.patch_btn.configure(state="disabled")
    
    def _apply_patch(self):
        path = Path(self.game_path.get())
        
        if not path.exists():
            messagebox.showerror("Error", "La carpeta seleccionada no existe.")
            return
        
        # Find game/ directory
        game_dir = path / "game"
        if not game_dir.exists():
            # Maybe user selected the game/ subfolder directly
            if (path / "script.rpa").exists():
                game_dir = path
            else:
                messagebox.showerror(
                    "Error",
                    "No se encontro la carpeta 'game/' dentro de la ruta seleccionada.\n\n"
                    "Asegurate de seleccionar la carpeta raiz del juego "
                    "(donde esta HighwayBlossoms.exe)."
                )
                return
        
        if not PARCHE_DIR.exists():
            messagebox.showerror("Error", "No se encontraron los archivos del parche. Reinstala el parcheador.")
            return
        
        try:
            self.progress_var.set(0)
            self.progress.start(10)
            self.patch_btn.configure(state="disabled")
            self.status_text.set("Aplicando parche...")
            self.root.update()
            
            # 1. Copiar archivos de traduccion (tl/spanish/)
            tl_source = PARCHE_DIR / "tl" / "spanish"
            tl_dest = game_dir / "tl" / "spanish"
            
            if tl_dest.exists():
                shutil.rmtree(tl_dest)
            
            shutil.copytree(tl_source, tl_dest)
            self.status_text.set(f"Copiados archivos de traduccion ({sum(1 for _ in tl_dest.rglob('*.rpy'))} archivos)...")
            self.progress_var.set(30)
            self.root.update()
            
            # 2. Copiar preferences.rpy
            pref_src = PARCHE_DIR / "preferences.rpy"
            pref_dst = game_dir / "preferences.rpy"
            shutil.copy2(pref_src, pref_dst)
            self.status_text.set("Instalado selector de idioma...")
            self.progress_var.set(60)
            self.root.update()
            
            # 3. Copiar spanish_locale.rpy
            loc_src = PARCHE_DIR / "spanish_locale.rpy"
            loc_dst = game_dir / "spanish_locale.rpy"
            shutil.copy2(loc_src, loc_dst)
            self.status_text.set("Registrado idioma espanol...")
            self.progress_var.set(80)
            self.root.update()
            
            # 4. Limpiar cache para forzar recarga
            for cache_file in game_dir.glob("cache/*.rpyb"):
                cache_file.unlink(missing_ok=True)
            
            self.progress_var.set(100)
            self.progress.stop()
            self.status_text.set("Parche aplicado correctamente.")
            
            messagebox.showinfo(
                "Completado",
                "La traduccion al espanol se ha instalado correctamente.\n\n"
                "Para jugar en espanol:\n"
                "1. Abre el juego\n"
                "2. Ve a Preferences > Language\n"
                "3. Selecciona 'Espanol'\n\n"
                "Si el juego ya estaba abierto, reinicialo."
            )
            
        except PermissionError:
            messagebox.showerror(
                "Error de permisos",
                "No se pudo escribir en la carpeta del juego.\n"
                "Ejecuta el parcheador como administrador o mueve el juego a una carpeta sin restricciones."
            )
        except Exception as e:
            self.progress.stop()
            messagebox.showerror("Error", f"Error al aplicar el parche:\n\n{str(e)}")
        finally:
            self.progress_var.set(0)
            self._validate_path()
    
    def run(self):
        self.root.mainloop()


def main():
    app = ParcheadorApp()
    app.run()


if __name__ == "__main__":
    main()
