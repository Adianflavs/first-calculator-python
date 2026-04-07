print("MY calculator")

N1 = int(input("Enter the Frst Number:"))
N2 = int(input("Enter The Second Number:"))

operation = input("Enter operation, ( +. -. *, /): ")

if operation == "+":
    print("Result:", N1 + N2)
elif operation == "-":
    print("Result:", N1 - N2)
elif operation == "*":
    print("Result:", N1 - N2)

elif operation == "/":
    if N2 != 0:
        print("Result:", N1 / N2)
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid operation")