import sys
while True:
    try:
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")
        if op == '+':
            res = n1 + n2
        elif op == '-':
            res = n1 - n2
        elif op == '/':
            res = n1 / n2
        elif op == '*':
            res = n1 * n2
        else:
            raise ValueError("Invalid operation")
        print("{0} + {1} = {2}".format(n1, n2, res))
    except:
        print("Error: ", sys.exc_info())
    finally:
        print("****************************")
        if input("Continue (y/n)?") != 'y':
            break;
