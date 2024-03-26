#!/usr/bin/env python3

class Estilo:
    """Estilo de texto, bold, italic..."""
    bold = "\x1b[1m"
    italic= "\x1b[3m"
    underline= "\x1b[4m"
    strike= "\x1b[9m"
    reset = "\x1b[0m"