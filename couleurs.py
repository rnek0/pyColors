#!/usr/bin/env python3
# Ejercicios de entrenamiento en el curso de Python Ofensivo hack4u.io
# 23-03-2024 / rnek0

class Banner:
    """Display banner app"""
    title = """\t    ____                                 __                    
\t   / __ \___  _________  _________ _____/ /___  ________  _____
\t  / / / / _ \/ ___/ __ \/ ___/ __ `/ __  / __ \/ ___/ _ \/ ___/
\t / /_/ /  __/ /__/ /_/ / /  / /_/ / /_/ / /_/ / /  /  __(__  ) 
\t/_____/\___/\___/\____/_/   \__,_/\__,_/\____/_/   \___/____/  
\t                                  Decoradores y propiedades\n\n"""

def secuencias_de_escape():
    """ Secuencias de escape ANSI """
    print()
    print(" [+] \\x1b[" "\tEmpieza la secuencia de escape.")      
    print(" [+] \\x1b[0m" "\tTermina la secuencia de escape.")
    print()

    for i in range(1,255):
        print(f"\x1b[38;5;{i}m{i}", end= " ")

    toto = "\n\nBonjour"
    print(f"\x1b[38;5;46m{toto}\x1b[0m à tous.\n\n")


class Estilo:
    """Estilo de texto, bold, italic..."""
    bold = '1m'
    italic= '3m'
    underline= '3m'
    strike= '3m'
    reset = '0m'

class Color:
    """Algunos colores"""
    fg = 7 # white
    verde = 46 #"\x1b[38;25;46m"
    azul = 25 #"\x1b[38;25;25m"
    rojo = 9 #"\x1b[38;25;9m"
    reset = 0 #'\x1b[0m'
    colors = [fg,verde, azul, rojo,reset]



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
            str_reset =  self.color(Color.reset)  #f"\x1b[{Color.reset}m"
           
            funcion(self, str_color + texto + str_reset, self._color)
            # print('\nSaliendo de la envoltura\n')
        return envoltura

    @con_color
    def escribe(self,texto,color=Color.fg):
        self._color = color
        print(f"{texto}", end= " ")
        

if __name__ == '__main__':
    #secuencias_de_escape()
    
    tui = TUI()
    tui.escribe(Banner.title, Color.rojo)
    tui.escribe("[+] Jugando con colores en el ejercicio de los decoradores...\n")
    tui.escribe("Hola \o/ ,",Color.azul)
    tui.escribe("soy rnek0",Color.verde)
    tui.escribe(", que tal ?",Color.rojo)
    print("\n")

