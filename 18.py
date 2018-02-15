while True:
    print("Настройки")
    print("Введите '+' для сложения")
    print("Введите '-' для вычетания")
    print("Введите '*' для умножения")
    print("Введите '/' для деления")
    print("Введите 'Выход' для выхода из калькулятора")
    user_input = input(":")
 
    def bring_numbers():
        num1 = float(input("Введите первое число: "))   
        num2 = float(input("Введите второе число: "))
        return num1,num2
    
    
 
    if user_input == "Выход":
        break
    elif user_input == "+":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        bring_numbers() 
        result = str(num1+num2)
        print ("Ответ: " + result)
    elif user_input == "-":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = str(num1-num2)
        print("Ответ: " + result) 
    elif user_input == "*":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = str(num1*num2)
        print("Ответ: " + result) 
    elif user_input == "/":            
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = str(num1/num2)
        print("Ответ: " + result) 
    else:
        print("неизвестный ввод")
