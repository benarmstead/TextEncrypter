import platform
import os

#checks platform and then clears the screen accordingly
def clr_sc():
    plat=platform.system()
    if plat=="Linux":
        os.system("clear")
    elif plat=="Windows":
        os.system("cls")
