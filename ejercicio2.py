while True:
    try:
        x = float(input("Ingrese primer número:")) 
        y = float(input("Ingrese segundo número:")) 
        r = x/y
        print("Respuesta: ", r)
    except ZeroDivisionError as ex:
        print(str(ex))
        print("Vuelve a intentarlo.")
    except ValueError as ex:
        print(str(ex))
        print("Vuelve a intentarlo.")
    else:
        print("Fin del programa.")
        break