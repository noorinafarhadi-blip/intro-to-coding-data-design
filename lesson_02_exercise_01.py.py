# Ask the user for the City name

City= input("Enter name of the city:")

# Ask the user for the  temperature in Fahrenheit
Fahrenhiet =  float(input("Enter the current temperature in Fahrenhiet: " ))

# Convert the temperature to Celsius.

Celsius = (Fahrenhiet- 32) * 5 / 9

# Check if the temperature is below Freezing
if Celsius < 0:
    print("Alert The temperature is below freezing point.")

else:
    print("The temperature is above the freezing point.")

# Print the temperature in Celsius
print(f"The current temperature in {City} is {Celsius:.1f} degree Celsius.")
