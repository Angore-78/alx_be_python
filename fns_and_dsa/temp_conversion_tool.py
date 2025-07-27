FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(temperature):
         converted_temperature = (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
         return converted_temperature 


def convert_to_fahrenheit(temperature):
         converted_temperature = (temperature + 32) * CELSIUS_TO_FAHRENHEIT_FACTOR
         return converted_temperature


def main():
     try:
          temperature_input = input('Enter the temperature to convert: ')
          temperature = float(temperature_input)
     except ValueError:
            print('Kindly enter a numerical value.')
            return
     
     units = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').upper()
     if units=='C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f'{temperature} is {converted_temperature}')
     elif units=='F':
            converted_temperature=convert_to_celsius(temperature)
            print(f'{temperature} is {converted_temperature}')
     else:
            print('Invalid value for unit.')


if __name__ == "__main__":
       main()


        

    