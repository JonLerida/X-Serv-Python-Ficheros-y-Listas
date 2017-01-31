#!/usr/bin/python3

fd = open("/etc/passwd", "r")
#str.find("lo que buscas")-->busca y devuelve el índice
#str.rfind("lo que buscas") --> Eempieza a buscar por atras y devuelve el índice respecto al origen
lineas = fd.readlines()
for linea in lineas:
	login = linea[:linea.find(":")]
	shell = linea[linea.rfind(":")+1:-1]
	print(login, shell)
print("forma 1")		#str.split('x')--> separa en cadenas buscando el 'x'
for linea in lineas:
	login = linea.split(':')[0]
	shell = linea.split(':')[-1][:-1] #[-1]--> primer elemento de la lista
					  #[:-1]-->todos los elementos menos el último
	print(login, shell)
print("forma 2")
fd.close()

