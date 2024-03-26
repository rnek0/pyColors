#!/usr/bin/env python3
# Ejercicios de entrenamiento en el curso de Python Ofensivo hack4u.io
# 23-03-2024 / rnek0
# ANSI escape codes : https://en.wikipedia.org/wiki/ANSI_escape_code

from color import Color
from estilo import Estilo

class Banner:
    """Display banner app"""
    title = """
\t\t    ____                                 __                    
\t\t   / __ \___  _________  _________ _____/ /___  ________  _____
\t\t  / / / / _ \/ ___/ __ \/ ___/ __ `/ __  / __ \/ ___/ _ \/ ___/
\t\t / /_/ /  __/ /__/ /_/ / /  / /_/ / /_/ / /_/ / /  /  __(__  ) 
\t\t/_____/\___/\___/\____/_/   \__,_/\__,_/\____/_/   \___/____/  
\t\t                                  Decoradores y propiedades\n\n"""

def secuencias_de_escape():
    """ Secuencias de escape ANSI """
    ansi = "\n [+] Códigos escape ANSI :"
    explicacion = """se utilizan para dar formato a la salida de una terminal de texto 
      y se basan en un estándar ANSI, ANSI X3.64 (también denominado ECMA-48)."""
    print(f"\x1b[38;5;46m{ansi}\x1b[0m {explicacion}")
    print()
    print(" [+] \\x1b[" "\tEmpieza la secuencia de escape.")      
    print(" [+] \\x1b[0m" "\tTermina la secuencia de escape.")

    for i in range(0,255):
        if i % 15 == 0:
            print('\n')
        value = f"\x1b[38;5;{i}m {i: <3}" # Aqui el posicionamiento de los int en columnas con ': <3' al final.
        print(f"{value}", end= " ")

    


class TUI:

    def color(self, u_char):
        """Return ASCII color code from int between 0-255"""
        return f"\x1b[38;5;{u_char}m"

    def __init__(self, element="", color=0):
        self._element = element
        if color:
            self._color = color
        else:
            self._color = Color.fg # ascii reset color code (here int 0)
            
        self.escribe(element,self._color)
    

    def con_color(funcion):
        # escribe tiene un parámetro opcional, se debe especificar aquí también.
        def envoltura(self,texto, _color=Color.fg):  
            # print('\nEntrando en la envoltura\n')
            str_color =  self.color(_color)       #f"\x1b[38;5;{_color}m"
            str_reset =  "\x1b[0m" #self.color(Color.reset)  #f"\x1b[{Color.reset}m"
           
            funcion(self, f"{str_color}{texto}{str_reset}", self._color)
            # print('\nSaliendo de la envoltura\n')
        return envoltura

    @con_color
    def escribe(self,texto,color=Color.fg):
        self._color = color
        print(f"{texto}", end= " ")
        

if __name__ == '__main__':
    tui = TUI()
    tui.escribe(Banner.title, Color.rojo)
    
    pregunta = f"\n [!] Quieres ver {Estilo.bold}los colores ANSI ?{Estilo.reset} [y/n] : "
    ver = input(pregunta)
    if ver == "y":
        secuencias_de_escape()
    
    tui.escribe(f"\n\n[+] {Estilo.bold}Jugando con colores{Estilo.reset} en el ejercicio de {Estilo.underline}los decoradores{Estilo.reset}...\n")
    tui.escribe(f"Hola \o/ ,",Color.azul)
    tui.escribe(f"soy rnek0",Color.verde)
    tui.escribe(f", que tal ?",Color.rojo)
    print("\n")

