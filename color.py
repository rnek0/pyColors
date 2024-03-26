#!/usr/bin/env python3

class Color:
    """Algunos colores"""
    fg = 7 # white
    verde = 46 #"\x1b[38;25;46m"
    azul = 25 #"\x1b[38;25;25m"
    rojo = 9 #"\x1b[38;25;9m"
    reset = 0 #'\x1b[0m'
    colors = [fg,verde, azul, rojo,reset]