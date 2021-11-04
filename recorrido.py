def run():
    nombre = input("Escribe tu nombre: ")
    nombre = nombre.replace(' ', '').upper()
    i = 0
    for letra in nombre:
        i += 1
        print("La letra número " + str(i) + " del nombre que ingresaste es: " + letra)
    print("El nombre ingresado tiene " + str(i) + " letras")        


if __name__ == '__main__':
    run()