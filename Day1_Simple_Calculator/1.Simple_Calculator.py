# DAY -1 Simple Calculator 

# Taking inputs from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

# writing the operation based on the operator
try:
    if operator=='+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        # for division by zero
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result= a/b
    else:
        # If operator is invalid
        print("Invalid operator")
        result="Somrthing Wrong"
        
        # Displaying the result
    if result != "Somrthing Wrong":
       print("Result is:", result)
   
except ZeroDivisionError as exe:
  
    print(exe)
except   ValueError:
    print("Please enter valid numeric values")
