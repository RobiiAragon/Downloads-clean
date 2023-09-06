import os
import shutil
import customtkinter as ctk
import tkinter
from tkinter import filedialog

def acomodar_archivos():
    # Obtener la carpeta de origen (donde están los archivos para acomodar)
    carpeta_origen = filedialog.askdirectory(title="Selecciona la carpeta de origen")

    if not carpeta_origen:
        return

    # Carpeta de destino para cada tipo de archivo (pones tus rutas segun tus criterio)
    carpetas_destino = {
        'Videos': r'D:\videos',
        'Fotos': r'C:\Users\jesus\Imágenes',
        'ZIP': r'C:\Users\jesus\Documentos',
        'EXE': r'D:\InstaladoresEXE\jesus\Documentos'
    }

    for nombre_archivo in os.listdir(carpeta_origen):
        archivo_completo = os.path.join(carpeta_origen, nombre_archivo)
        if os.path.isfile(archivo_completo):
            extension = nombre_archivo.split('.')[-1].upper()
            destino = carpetas_destino.get(extension, r'C:\Users\jesus\Otro')
            shutil.move(archivo_completo, os.path.join(destino, nombre_archivo))

    print("Archivos acomodados con éxito!")

# Crear la ventana principal de la aplicación
root = ctk.CTk()
root.title("Acomodar Archivos by Robii Aragon")
root.geometry("300x200")
root.iconbitmap('APP/ico.ico')

# Crear un botón personalizado en la ventana
boton_acomodar = ctk.CTkButton(root, text="Acomodar", command=acomodar_archivos)
boton_acomodar.pack(expand=True, fill='both', padx=5, pady=5)

# Ejecutar la aplicación
root.mainloop()
