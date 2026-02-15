def add(op1, op2):
    return op1 + op2

def sub(op1, op2):
    return op1 - op2

def mul(op1, op2):
    return op1 * op2

def div(op1, op2):
    return op1 / op2 if op2 != 0 else "Error : Division by 0 is not allowed"

if __name__ == "__main__":
    print("--------------Simple Calculator--------------")
    while True:
        operator = int(input("1.Addition(+)   2.Subtraction(-)   3.Multiplication(*)   4.Division(/)   5.Exit\nChoice : "))
        if operator == 5:
             exit()
        while operator > 5:
            operator = int(input("Choose a correct option(1,2,3,4,5) : "))
        try:
            operand1 = int(input("Enter operand 1 : "))
            operand2 = int(input("Enter operand 2 : "))
            if operator == 1:
                    print(f"Addition of {operand1} & {operand2} is {add(operand1,operand2)}\n")
            elif operator == 2:
                    print(f"Subtraction of {operand1} & {operand2} is {sub(operand1,operand2)}\n")
            elif operator == 3:
                    print(f"Multiplication of {operand1} & {operand2} is {mul(operand1,operand2)}\n")
            elif operator == 4:
                    print(f"Division of {operand1} & {operand2} is {div(operand1,operand2)}\n")
        except:
            print("Value Error : Enter numerical values")