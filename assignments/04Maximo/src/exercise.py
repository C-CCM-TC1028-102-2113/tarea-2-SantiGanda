def main():
    #escribe tu código abajo de esta línea
    
num1= int(input("Dame un número "))
num2= int(input("Dame un número "))
num3= int(input("Dame un número "))

if num1>num2 and num1>num3:
    print(str(num1))
elif num2>num3 and num2>num1:
    print(str(num2))
else:
    print(str(num3))

    pass


if __name__=='__main__':
    main()
