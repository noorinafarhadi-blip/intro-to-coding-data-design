#Exverise 3

#Ask the user for the city names
city1 = input("Please enter the name of the first city: ")
city2 = input("Please enter the name of the second city: ")

# Ask the user for the current temperture in Celsius
temperture1 = input(f"Please enter the current temperture for {city1}: ")
temperture2 = input(f"Please enter the current temperture for {city2}: ")

# Convert the tempertures to float
temperture1 = float(temperture1)
temperture2 = float(temperture2)

# Calculate the average temperture
average_temperture =(temperture1 + temperture2)/ 2

# Print the user input in a formatted string
print(f"The averate temperture between {city1} and {city2} is {average_temperture} degrees Celsius")

# Convert the average temperture to Fahrenhiet
fahrenheit = average_temperture * 9/ 5+ 32

# Print the temperature in Fahrenhiet
print(f"that's{fahrenheit, 1} degeers fahrenhiet.")
