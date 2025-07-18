#Provides multiplication table of numerical inputs from 1 to 10
number =(input('Enter a number to see its multiplication table: '))
for number_input in number:
        for value in range(1,11):
            print(f"{number} * {value} = {int(number) * value}")