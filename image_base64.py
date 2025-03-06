import base64
import tkinter as tk
from tkinter import filedialog

def select_image():
    """Abre un cuadro de diálogo para seleccionar una imagen y devuelve su ruta"""
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana de Tkinter
    file_path = filedialog.askopenfilename(title="Seleccionar imagen", filetypes=[("Imágenes", ("*.png", "*.jpg", "*.jpeg", "*.gif"))])
    return file_path

def encode_image_to_base64(image_path):
    """Codifica una imagen en Base64 y la guarda en un archivo .txt"""
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    with open("encoded_image.txt", "w") as text_file:
        text_file.write(encoded_string)
    print("✅ Imagen codificada y guardada en 'encoded_image.txt'")
    return encoded_string

def decode_base64_to_image(output_path):
    """Lee la cadena Base64 desde el archivo .txt, la decodifica y guarda la imagen"""
    with open("encoded_image.txt", "r") as text_file:
        base64_string = text_file.read()
    image_data = base64.b64decode(base64_string)
    with open(output_path, "wb") as image_file:
        image_file.write(image_data)
    print(f"✅ Imagen guardada en: {output_path}")

if __name__ == "__main__":
    # Paso 1: Seleccionar imagen
    image_path = select_image()
    if image_path:
        print(f"Imagen seleccionada: {image_path}")

        # Paso 2: Codificar en Base64 y guardar en un txt
        encode_image_to_base64(image_path)

        # Paso 3: Decodificar desde el txt y guardar la imagen
        output_image_path = "decoded_image.png"
        decode_base64_to_image(output_image_path)
    else:
        print("No se seleccionó ninguna imagen.")