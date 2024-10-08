#David Ramirez 
#10/8/2024
anw = float(input("Insert your degrees in Fahrenheit "))
num1 = 30
num2 = 70
celsius = (anw-32)*5/9
celsius = round(celsius, 2)
if anw<num1:
    print("That’s cold! In Norway you would say it is",anw,"degrees and", celsius,"celsius")
elif anw>num1:
    print("“That’s hot! In Brazil you would say it is",anw, "degrees and", celsius, "celsius")
elif anw>num1>num2:
    print("That’s Balmy! In Japan you would say it is",anw,"degrees and", celsius, "celsius")
#This program compares the users input with two other variables, converting to celsius