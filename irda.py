#!/usr/bin/python3
print('\033[31m')
print("""
 █████╗ ██████╗  █████╗ ███╗  ██╗ █████╗  ██████╗
██╔══██╗██╔══██╗██╔══██╗████╗ ██║██╔══██╗██╔════╝
██║  ╚═╝██████╔╝██║  ██║██╔██╗██║██║  ██║╚█████╗
██║  ██╗██╔══██╗██║  ██║██║╚████║██   ██║ ╚═══██╗
╚█████╔╝██║  ██║╚█████╔╝██║ ╚███║╚█████╔╝ ██████╔
 ╚════╝ ╚═╝  ╚═╝ ╚════╝ ╚═╝ ╚══╝ ╚════╝   ╚═════╝
                          by:Franck-C * David-hk4
""")
import sys
import os
import time

jpg = ".jpg/"

dni = input("Intoduce el número de dni: ")

print("""

 [1] Foto del dni
 [2] Firma del dni
 [3] Huellas digitales

""")
opcion = input("Elige una opción: ")

if opcion == "1":
    os.system("wget http://www.enlacesframework.info/vfpsapirenic/images/foto/" + dni + jpg)

elif opcion == "2":
    os.system("wget http://www.enlacesframework.info/vfpsapirenic/images/firma/" + dni + jpg)

elif opcion == "3":
    os.system("wget http://www.enlacesframework.info/vfpsapirenic/images/huellas/d" + dni + jpg)
    os.system("wget http://www.enlacesframework.info/vfpsapirenic/images/huellas/i" + dni + jpg)

else:
    print("Opcion incorrecta x_x")

