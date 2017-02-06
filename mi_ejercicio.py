#!/usr/bin/python3

fd = open("/etc/passwd", "r")             #Lo abrimos en lectura solo, si no da error

lineas = fd.readlines()
usuarios = {}
for line in lineas:
    login = line[:line.find(":")]
    shell = line[line.rfind(":")+1:]
    usuarios[login]= shell

#try--except controla las excepciones
#si solo pones except te sirve para cualquier excepcion
#si ponesalguna excepción solo se fija en esa
try:
    print('root', usuarios['root'])
    print("---\n")
    print('imaginario', usuarios['imaginario'])
except KeyError:
    print("ERROR!\nEl usuario no existe")
    raise SystemExit
