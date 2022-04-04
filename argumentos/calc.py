#!/usr/bin/python3

import sys
import getopt

opc ,argus = getopt.getopt(sys.argv[1:],'o:n:m:')

operador = ""
numeros = []

for o in opc:
    for i in o:
        if i == "-o":
            operador = o[1]
        elif i == "-n":
            numeros.append(o[1])
        elif i == "-m":
            numeros.append(o[1])

if operador == "+":
    print ("el resultado de la suma es: ", int(numeros[0])+int(numeros[1]))
if operador == "-":
    print ("El resultado de la resta es ", int(numeros[0])-int(numeros[1]))
if operador == '*':
    print ("el resultado de la multiplicacion es:", int(numeros[0])*int(numeros[1]))
if operador == "/":
    print ("el resultado de la divison es:", int(numeros[0])/int(numeros[1]))
else:
     sys.exit()
