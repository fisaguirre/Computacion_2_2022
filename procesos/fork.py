#!/usr/bin/python3

import os
import argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument('--n', required=True, type=int, dest="cantidad_procesos", default = 2,
	                    help='Escriba el numero de procesos hijos')
parser.add_argument('--h', dest="ayuda",
	                    help='Ayuda')
parser.add_argument('--v', dest = "verboso", action="store_true",
	                    help='Modo verboso')

args = parser.parse_args()


def suma(pid, ppid):
    #print ("Esta es la función suma de pares")
    suma = 0
    for number in range(1, pid+1):
        if(number % 2 == 0):
            suma = suma + number
    print ("Suma:", str(pid) + " - " + str(ppid) + " = " + str(suma))
    

for numero in range(args.cantidad_procesos):
    pid = os.fork()
    if pid == 0:
        if args.verboso:
            print("Starting process: ", os.getpid())
        suma(os.getpid(), os.getppid())
        if args.verboso:
            print("Ending process:", os.getpid())
        exit()
        #os._exit(0)
    else:
        os.wait()
        