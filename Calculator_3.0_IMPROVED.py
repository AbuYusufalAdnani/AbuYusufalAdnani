print("-------Welcome to the Calculator 3.0 IMPROVED!-------")

while True:
    
    Operation = input("Select what operation you want to perform (division = /, multiplication = *, addition = +, and subtraction = -) \n \n / \n * \n + \n - \n \n --Answer-- \n \n")

    if Operation == "+":
        Addition1 = input("Enter a number (to add): ")
        Addition2 = input("Enter a number (to add): ")
        AdditionResult1 = float(Addition1)
        AdditionResult2 = float(Addition2)
        Addition1
        Addition2
        AdditionResultFinal = AdditionResult1 + AdditionResult2
        print("The result of the addition is: ", AdditionResultFinal)
    else:
        print("Rendering mathematical operation...")

        if Operation == "/":
            Addition1 = input("Enter a number (to divide): ")
            Addition2 = input("Enter a number (to divide): ")
            AdditionResult1 = float(Addition1)
            AdditionResult2 = float(Addition2)
            Addition1
            Addition2
            AdditionResultFinal = AdditionResult1 / AdditionResult2
            print("The result of the division is: ", AdditionResultFinal)
        else:
            print("Rendering mathematical operation...")

        if Operation == "*":
            Addition1 = input("Enter a number (to multiply): ")
            Addition2 = input("Enter a number (to multiply): ")
            AdditionResult1 = float(Addition1)
            AdditionResult2 = float(Addition2)
            Addition1
            Addition2
            AdditionResultFinal = AdditionResult1 * AdditionResult2
            print("The result of the multiplication is: ", AdditionResultFinal)
        else:
            print("Rendering mathematical operation...")
        if Operation == "-":
            Addition1 = input("Enter a number (to subtract): ")
            Addition2 = input("Enter a number (to subtract): ")
            AdditionResult1 = float(Addition1)
            AdditionResult2 = float(Addition2)
            Addition1
            Addition2
            AdditionResultFinal = AdditionResult1 - AdditionResult2
            print("The result of the subtract is: ", AdditionResultFinal)
        else:
            print("Rendering mathematical operation...")