FirstNumber = int(input("Enter the first number: "))

SecondNumber = int(input("Enter the second number: ")) 

Operation = int(input(f"Choose the operation you want to perform: (Choose a number from 1 to 4)\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n"))

if Operation == 1:
    print(f"The sum of {FirstNumber} and {SecondNumber} is: {FirstNumber + SecondNumber}")
elif Operation == 2:
    print(f"The difference between {FirstNumber} and {SecondNumber} is: {FirstNumber - SecondNumber}")
elif Operation == 3:
    print(f"The product of {FirstNumber} and {SecondNumber} is: {FirstNumber * SecondNumber}")
elif Operation == 4:
    print(f"The quotient of {FirstNumber} and {SecondNumber} is: {FirstNumber / SecondNumber}")
else:
    print("Please enter a valid operation.")