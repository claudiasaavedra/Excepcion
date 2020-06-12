while True:
    try:
        x = float(input("Ingrese un número:"))
    except ValueError as ex:
        print(str(ex))
        print("Ingrese un número por favor.")
        # raise
    else:
        print("Ingresó un número válido.")
        break