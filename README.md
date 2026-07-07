# Parcheador de traduccion al espanol para Highway Blossoms

# Aviso Importante y Legal

## Traducción 100% Gratuita:
Este parche es un proyecto hecho de fans para fans y su distribución es completamente gratuita. Queda estrictamente prohibida su venta o comercialización. Si pagaste por esta traducción o la descargaste de un sitio de pago, te han estafado.

## Requiere juego Original:
Para utilizar estas herramientas y aplicar el parche, es requisito indispensable que utilices una copia de seguridad (de tu compra) extraída de tu propio juego original. Este proyecto NO incluye, distribuye ni enlaza a ROMs o ISOs con derechos de autor. Por favor, apoya a los desarrolladores originales; en caso de que una versión traducida oficial por parte de la compañía sea licenciada en tu país, favor de borrar esta versión y adquirir la original.



## Version compatible
Highway Blossoms 1.3.1 

## Uso
1. Ejecuta `HB_Parcheador_ES_v1.0.exe`
2. Selecciona la carpeta donde instalaste el juego (donde esta `HighwayBlossoms.exe`)
3. Haz clic en "Aplicar Parche"
4. Abre el juego, ve a Preferences > Language > Espanol

## Compilar el .exe
```bash
pip install pyinstaller
bash build.sh
```

## Estructura
```
parcheador/
├── parcheador.py          # Aplicacion con UI (tkinter)
├── build.sh               # Script para compilar .exe
├── requirements.txt
├── parche/                # Archivos que se copian al juego
│   ├── tl/spanish/        # 86 archivos de traduccion
│   ├── preferences.rpy    # Selector de idioma modificado
│   └── spanish_locale.rpy # Registro del locale
└── README.md
```

## Creditos
Traduccion por fans. Highway Blossoms (c) Studio Elan.
