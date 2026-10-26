while True:
    try:
        
        n1 = int(input("What is number 1? : "))
        n2 = int(input("What is number 2? : "))
        arithmetic_Operator = input("What arithmethic function (+ - / * ^)? : ")

        if arithmetic_Operator == "+":
            print(n1 + n2)
        elif arithmetic_Operator == "-":
            print(n1 - n2)
        elif arithmetic_Operator == "/":
            print(n1 / n2)
        elif arithmetic_Operator == "*":
            print(n1 * n2)
        elif arithmetic_Operator == "^":
            print(n1 ** n2)
            
    except ValueError:
        break