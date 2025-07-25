def perform_operation(num1, num2, operation):
    if operation == 'add' :  
        result = float(num1) + float(num2)
    elif operation == 'subtract' : 
        result = float(num1) - float(num2)
    elif operation == 'multiply' :
        result = float(num1) * float(num2)
    elif operation == 'divide': 
        result = float(num1) / float(num2)
    elif operation == 'divide' and num2 == 0:
        result = "Sorry, but you can't divide by zero"

    return result

        
from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()           
#calculate = perform_operation(12,0,'divide')
#print(calculate)


         

