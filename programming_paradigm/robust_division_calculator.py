def safe_divide(numerator, denominator):
    try :
        quotient = f"The result of the division is {float(numerator) / float(denominator)}"
        return quotient 
    except ZeroDivisionError:
        message = "Error: Cannot divide by zero."
        return message
    except ValueError:
        message = 'Error: Please enter numeric values only.'
        return message


import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()

    
    
