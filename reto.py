def run():
    vidas = 3
    respuesta = input("Blanca por dentro, verde por fuera. Si no sabes, espera ¿qué es? (tienes 3 intentos): ")
    respuesta = respuesta.lower()
    correcta = "pera"
    while vidas > 0:
        if respuesta != correcta:
            print("Usted ha respondido de manera incorracta, ahora tiene " + str(vidas) + " intentos.")
            vidas -= 1
            respuesta = input("Blanca por dentro, verde por fuera. Si no sabes, espera ¿qué es?: ")
        else:
            print("Usted ha respondido correctamente. :)")
            break



if __name__ == '__main__':
    run()