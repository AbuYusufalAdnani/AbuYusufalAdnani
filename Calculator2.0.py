print("-------Welcome to the Calculator!-------")

while True:
    CA1 = input("Enter a number to subtract (this following code will subtract with the next line): ")
    CA2 = input("Enter a number to subtract (to subtract with the previous number): ")
    result1 = float(CA1)
    result2 = float(CA2)
    result = result1 - result2
    print("The following answer is: ", result)