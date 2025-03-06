# 📷 Convertidor de Imágenes a Base64 en Python

Este script en Python permite:

✅ **Leer una imagen** desde el sistema de archivos.  
✅ **Codificarla en Base64** y guardar el código en un archivo `.txt`.  
✅ **Decodificar el código Base64** para regenerar la imagen original.

## 📌 Requisitos

Asegúrate de tener **Python 3** instalado. Además, el script usa la biblioteca estándar `tkinter`, que debe estar incluida en tu instalación de Python. Si usas **Arch Linux**, instala `tkinter` con:

```bash
sudo pacman -S tk
```

## 🚀 Instalación y Uso

1. **Clona este repositorio** o descarga el archivo `image_base64.py`:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. **Ejecuta el script** en tu terminal o en PyCharm:
   ```bash
   python image_base64.py
   ```

3. **Selecciona una imagen** cuando aparezca la ventana de diálogo.

4. **La imagen será codificada en Base64** y el código se guardará en `encoded_image.txt`.

5. **El código Base64 será decodificado** y se generará la imagen `decoded_image.png`.

## 📜 Código de Ejemplo

```python
import base64
import tkinter as tk
from tkinter import filedialog

def select_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Seleccionar imagen",
        filetypes=[("Imágenes", ("*.png", "*.jpg", "*.jpeg", "*.gif"))]
    )
    return file_path

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    with open("encoded_image.txt", "w") as text_file:
        text_file.write(encoded_string)
    return encoded_string

def decode_base64_to_image(output_path):
    with open("encoded_image.txt", "r") as text_file:
        base64_string = text_file.read()
    image_data = base64.b64decode(base64_string)
    with open(output_path, "wb") as image_file:
        image_file.write(image_data)

if __name__ == "__main__":
    image_path = select_image()
    if image_path:
        encode_image_to_base64(image_path)
        decode_base64_to_image("decoded_image.png")
```

## 📝 Notas

- Si no aparece la ventana de selección de imágenes en **Linux**, asegúrate de ejecutar PyCharm o la terminal con `DISPLAY` configurado correctamente.
- El código Base64 generado puede ser usado para almacenamiento, transmisión o incrustación en HTML/CSS.

---

