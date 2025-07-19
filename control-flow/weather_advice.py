#Receives weather input for the day and gives clothing recommendations
weather_input = input("What's the weather like today? (sunny/rainy/cold):")
#Conditions for clothing recommendations based on the weather input
if weather_input == 'sunny' :
    print("Wear a t-shirt and sunglasses.")
elif weather_input == 'rainy' : 
    print("Don't forget your umbrella and a raincoat.")
elif weather_input == 'cold':
    print("Make sure to wear a warm coat and scarf.")

else:
    print("Sorry I don't have recommendations for this weather.")
    