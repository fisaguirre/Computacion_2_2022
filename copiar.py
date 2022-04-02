#!/usr/bin/python3

import argparse
import os.path

def parse():
	parser = argparse.ArgumentParser()
	parser.add_argument('--i', required=True, dest="existente", 
	                    help='Escriba el nombre del archivo existente')
	parser.add_argument('--o', required=True, dest = "nuevo", 
	                    help='Escriba el nombre del archivo nuevo')
	return parser.parse_args()
    
def verifyFile(args):
    if os.path.isfile(args.existente):
        copyText(args)
    else:
        print ("File not exist")

def copyText(args):
    with open(args.existente,'r') as firstfile, open(args.nuevo,'w+') as secondfile:
        for line in firstfile:
             secondfile.write(line)

if __name__ == "__main__":
    argumentos = parse()
    verifyFile(argumentos)