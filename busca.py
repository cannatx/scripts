#!/usr/bin/env python3
import os

find_str = input('Que quieres buscar?\n')
# find_str = 'Video'
dir_to_look = './__ENTEL__/'
dest = './__02_SALIDA_ORDENADOR/'

def busca(path,look):
    res = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if look.lower() in file.lower():
                res.append(os.path.join(root,file))
    return res

def mueve(files,dest):
    for file in files:
        cmd = 'mv -vf "{}" "{}"'.format(file,dest)
        os.system(cmd)

def main():
    archivos = busca(dir_to_look,find_str)
    if archivos == []:
        res = 'NO ENCONTRADO'
        print(res)
        return res
    else:
        mueve(archivos,dest)
        res = 'COMPLETADO'
        print(res)
        return res

if __name__ == "__main__":
    main()
