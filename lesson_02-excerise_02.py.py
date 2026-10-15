# Excersie 2

# Ask the user fo the city names
City1 = input("Please enter the name of the first city: ")
City2= input("Please enter the name of the second city: ")

# Ask the user for the current temperture in Celsius
temperture1 = input("Please enter the current temperture for " + City1 +": ")
temperture2 = input("Please enter the current temperture for " + City2 +" : ")

# Convert the temeratures to Float
temperture1 = float(temperture1)
temperture2 = float(temperture2)

# Calculate the average temperature
average_temperture =(temperture1 + temperture2) /2

# Print the average temperature
print("the average temperature between " + City1 + " and " + City2 + " is " + str(average_temperture) + "degrees Celsius.")

