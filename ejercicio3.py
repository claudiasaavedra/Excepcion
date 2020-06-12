lista = [1,3,7,9,15]
try:
    lista[10]
except IndexError as ex:
    print(str(ex))
else:
    print("Fin del programa.")