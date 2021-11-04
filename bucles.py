## Mi ejercicio
# def bucle(potencia, cantidad):
#     for i in range(cantidad):
#         calculo = potencia ** i
#         print(str(potencia) + " elevado a la " + str(i) + " es igual a " + str(calculo))




def run():
    ## Mi ejercicio
    # potencia = int(input("¿De qué número quieres ver las potencias?: "))
    # cantidad = int(input("¿Cuantas potencias quieres ver?: "))
    # print("Las potencias de " + str(potencia) + " son:")
    # bucle(potencia, cantidad)
    LIMITE = 1000000
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print("2" + " elevado a la " + str(contador) + " es igual a " + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador

if __name__ == '__main__':
    run()