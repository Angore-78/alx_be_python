from datetime import * 
def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'Current date and time: {current_date}')

def calculate_future_date():
    days_input = input('Enter the number of days to add to the current date: ')
    number_of_days = int(days_input)
    current_date = datetime.now().time
    future_date = current_date +  int(timedelta(days=number_of_days))
    print(f'Future date: {future_date.strftime('%Y-%m-%d')}')

display_current_datetime()
calculate_future_date()