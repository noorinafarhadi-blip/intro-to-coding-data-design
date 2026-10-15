# Ask the user for the City name

City1= input("Enter name of the city1:")

City2= input("Enter name of the city2:")


# Ask the user for the  temperature in Fahrenheit
Fahrenhiet1 =  float(input("Enter the current temperature in Fahrenhiet for " + City1 +": " ))
Fahrenhiet2 =  float(input("Enter the current temperature in Fahrenhiet for " + City2 +": " ))



# Convert the temperature to Celsius.

Celsius1 = (Fahrenhiet1- 32) * 5 / 9
Celsius2 = (Fahrenhiet2- 32) * 5 / 9


# Check if the temperature is below Freezing
if Celsius1 < 0 and Celsius2 < 0:

 print("Alert: The temperature is below freezing point.")

elif Celsius1 < 0 or Celsius2 < 0 :
   print("Alert: The temperature in one the cities are below freezing point.")

else:
    print("The temperature in both cities are above the freezing point.")

# Print the temperature in Celsius
print(f"The current temperature in {City1} is {Celsius1:.1f} degree Celsius.")
print(f"The current temperature in {City2} is {Celsius2:.1f} degree Celsius.")
