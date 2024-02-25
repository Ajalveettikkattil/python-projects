# CALCULATOR

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def muliple(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

while True:
    print("###############")
    print("Calculator")
    print("1: Add")
    print("2. Substract")
    print("3: Multiplication")
    print("4: Division")
    print("5: Quit")

    option = input("Select your option: 1,2,3,4,5: ")

    if option == '5':
        print("Exiting Program....!")
        break
    if option in('1','2','3','4'):
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        
        if option == '1':
            print("Result: ", add(num1,num2))
        elif option == '2':
            print("Result: ", sub(num1,num2))
        elif option == '3':
            print("Result: ", muliple(num1,num2))
        elif option == '4':
            print("Result: ", divide(num1,num2))
            
    else:
        print("Invalid option selected: ")
