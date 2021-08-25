
def main():
    #Escribe tu código debajo de esta línea
    
Edad=int(input("Dame tu edad "))
Licencia=input("¿Tienes licencia? s o n ")

if Edad < 18:
    print("No cumples con los requisitos")

elif Edad >= 18:
        if Licencia == "s":
            print("Trámite de la Licencia concedido")
        elif Licencia == "n":
            print("No cumples con los requisitos")
        else:
            print("Respuesta incorrecta")

    pass


if __name__ == '__main__':
    main()
