FirstNumber = int(input("Enter the first number: "))

SecondNumber = int(input("Enter the second number: ")) 

Operation = input(f"What operation do you want to perform on {FirstNumber} and {SecondNumber}? ")

if Operation == "addition":
    print(f"The sum of {FirstNumber} and {SecondNumber} is: {FirstNumber + SecondNumber}")
elif Operation == "subtraction":
    print(f"The difference between {FirstNumber} and {SecondNumber} is: {FirstNumber - SecondNumber}")
elif Operation == "multiplication":
    print(f"The product of {FirstNumber} and {SecondNumber} is: {FirstNumber * SecondNumber}")
elif Operation == "division":
    print(f"The quotient of {FirstNumber} and {SecondNumber} is: {FirstNumber / SecondNumber}")
else:
    print("Please enter a valid operation.")