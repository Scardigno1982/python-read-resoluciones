# PDF Number Extractor

Este proyecto permite extraer números específicos de documentos PDF, especialmente útil cuando el número está incrustado como una imagen.

## Requisitos

- Python 3.x
- Tesseract OCR
- Librerías Python: `pdf2image`, `pytesseract`, `PyPDF2`

## Instalación

1. Clona este repositorio:

git clone https://github.com/Scardigno1982/python-read-resoluciones.git
cd [NOMBRE_DEL_REPOSITORIO]


2. Instala las dependencias:

pip install pdf2image pytesseract PyPDF2


3. Instala Tesseract OCR. En sistemas basados en Debian/Ubuntu:
   
sudo apt-get install tesseract-ocr

## Uso

1. Ejecuta el script `pdfreader.py`:


## Uso

1. Ejecuta el script `pdfreader.py`:


2. El script buscará el número después de la etiqueta "Número:" y lo imprimirá en la consola.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir lo que te gustaría cambiar o añadir.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)

