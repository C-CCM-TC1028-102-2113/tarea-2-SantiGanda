def main():
    # Escribe el código adecuado para completar el programa
    
num1= int(input("Dame un número "))
num2= int(input("Dame un número "))
num3= int(input("Dame un número "))

if num1>num2 and num1>num3:
    print(str(num1))
    if num2>num3:
        print(str(num2))
        print(str(num3))
    else:
        print(str(num3))
        print(str(num2))

elif num2>num1 and num2>num3:
    print(str(num2))
    if num3>num1:
        print(str(num3))
        print(str(num1))
    else:
        print(num1)
        print(num3)

elif num3>num2 and num3>num1:
    print(num3)
    if num2>num1:
        print(num2)
        print(num1)
    else:
        print(num1)
        print(num2)

    pass


if __name__=='__main__':
    main()
