# simple_calculator.py

class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self,a,b):
        """Return the addition of a and b."""
        return  a  + b

    def subtract(self,a,b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self,a,b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self,a,b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b
    

#calculate = SimpleCalculator(12,8)
#print(calculate.add(12,8))
#print(f"Adding 5 to 7 is {calculate.add(5,7)}.Subtracting 100 from 35 is {calculate.subtract(35,100)}.\Multiplying 20 by 30 is"
    #  f"{calculate.multiply(20,30)}\nDivision by zero is {calculate.divide(12,0)}.")