#!/usr/bin/python3

import os
import argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument('-n', "--numero", type=int, dest="cantidad_procesos", default = 2,
	                    help='Escriba el numero de procesos hijos que desea')
parser.add_argument('-v', "--verbose", dest = "verbose", action="store_true",
	                    help='Habilitar modo verboso para mostrar el ciclo de vida de los procesos hijos')

args = parser.parse_args()


def suma(pid, ppid):
    suma = 0
    for number in range(1, pid+1):
        if(number % 2 == 0):
            suma = suma + number
    print ("Suma:", str(pid) + " - " + str(ppid) + " = " + str(suma))

for numero in range(args.cantidad_procesos):
    pid = os.fork()
    if pid == 0:
        if args.verbose:
            print("Starting process: ", os.getpid())
        suma(os.getpid(), os.getppid())
        if args.verbose:
            print("Ending process:", os.getpid())
        exit()
        #os._exit(0)
    else:
        os.wait()