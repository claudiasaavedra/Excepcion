import logging
from datetime import datetime, date
logging.basicConfig(filename='test.log', filemode='w', level=logging.DEBUG)

while True:
    try:
        x = float(input("Ingrese un número:"))
    except ValueError as ex:
        print(str(ex))
        logging.warning(str(ex), datetime.now().strftime('%d/%m/%Y/%H'))
        print("Ingrese un número por favor.")
    else:
        print("Ingresó un número válido.")
        logging.info("Fin del programa"+ '' + datetime.now().strftime('%d/%m/%Y/%H'))
        break