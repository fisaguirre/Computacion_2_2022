#!/usr/bin/python3

import os
import argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument('--n', required=True, type=int, dest="cantidad_procesos", default = 2,
	                    help='Escriba el numero de procesos hijos')
parser.add_argument('--h', dest="ayuda",
	                    help='Ayuda')
parser.add_argument('--v', dest = "verboso", 
	                    help='Modo verboso')

args = parser.parse_args()

def suma(pid):
    print ("esta es la función suma de pares")
    suma = 0
    for number in range(1, pid+1):
        if(number % 2 == 0):
            suma = suma + number
    print ("la suma es:", suma)

for numero in range(args.cantidad_procesos):
    pid = os.fork()
    if pid == 0:
        print ("el pid es:", pid, os.getpid(), os.getppid())
        print("se termina el hijo:" ,pid, os.getpid())
        suma(os.getpid())
        os._exit(0)

"""
listaProcesos = []
for numero in range(args.cantidad_procesos):
    pid = os.fork()
    print ("primero:", pid, os.getpid(), os.getppid())
    if pid == 0:
        listaProcesos.append(pid)
        print ("el pid es:", pid, os.getpid(), os.getppid())
    else:
        #os._exit(1)
"""