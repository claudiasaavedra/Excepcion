colores = {'rojo': 'red', 'verde': 'green', 'amarillo': 'yellow'}
try:
    print(colores['rojo'])
except KeyError as ex:
    print('Key Error:',str(ex))
else:
    print("Fin del programa.")