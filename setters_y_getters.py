#!/usr/bin/env python3
# Ejercicios de entrenamiento en el curso de Python Ofensivo hack4u.io
# 26-03-2024 / rnek0

import datetime
from color import Color

class Banner():
    _banner = """
\t    ____                   _          __          __         
\t   / __ \_________  ____  (_)__  ____/ /___ _____/ /__  _____
\t  / /_/ / ___/ __ \/ __ \/ / _ \/ __  / __ `/ __  / _ \/ ___/
\t / ____/ /  / /_/ / /_/ / /  __/ /_/ / /_/ / /_/ /  __(__  ) 
\t/_/   /_/   \____/ .___/_/\___/\__,_/\__,_/\__,_/\___/____/  
\t                /_/                                          
"""

    def __init__(self, fecha="26/03/2024"): # Constructor.
        self._fecha = fecha
        pass

    

    @property 
    def text(self): # Propriedad de solo lectura. (getter)
        return f"{self._banner}{' '*6}{'-'*35}-[ rnek0 {self._fecha} ]-{'-'*3}\n"


if __name__ == '__main__':
    fecha = datetime.datetime.now()
    banner = Banner(f"{fecha.today().day}/{fecha.today().month}/{fecha.today().year}")
    print(banner.text) # llama a la propriedad.