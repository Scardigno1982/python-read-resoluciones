# from pdfminer.high_level import extract_text

# text = extract_text('RES-2022-412.pdf')
# print(text)

# import PyPDF2

# with open('RES-2022-412.pdf', 'rb') as file:
#     reader = PyPDF2.PdfReader(file)
#     page = reader.pages[0]  # Primera página
#     text = page.extract_text()  # Extraer todo el texto de la primera página
    
#     # Tomar aproximadamente la primera mitad del texto
#     half_length = len(text) // 2
#     first_half = text[:half_length]
    
#     print(first_half)

from pdf2image import convert_from_path
import pytesseract
import re

# Convertir la primera página del PDF a imagen
images = convert_from_path('RES-2022-412.pdf', dpi=300, first_page=1, last_page=1)
first_page_image = images[0]

# Aplicar OCR a la imagen
text = pytesseract.image_to_string(first_page_image)

# Imprimir el texto extraído
# print(text)

# Si solo estás interesado en una parte de la imagen, puedes recortarla antes de aplicar OCR.



# ... [tu código anterior para extraer el texto con OCR] ...

# Usar una expresión regular para buscar el número después de "Número:"
match = re.search(r'Numero:\s*(\S+)', text)
if match:
    numero = match.group(1)
    print(numero)
else:
    print("Número no encontrado.")
