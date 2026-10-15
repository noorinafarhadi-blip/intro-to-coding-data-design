highest_temp = None
lowest_temp = None

highest_temp = ""
lowest_temp = ""

city = input("Please enter the name of the city: ")


while city.lower() != "exit":
 

    temperature_f = float(input(
        f"Please enter the current temperaturein Fahrenheit in{city}: "
    ))

    temperature_c =(temperature_f - 32) * 5 / 9

    print(
        f"The current temperature in {city} is "
        f"{temperature_f:g}°F or {temperature_c:.1f} °C"
 )

    if temperature_c < 0:
         print("Warning: The Temperature is below  freezing point.")
    

    if highest_temp is None:
       highest_temp = temperature_c
       highest_city = city

    if lowest_temp is None:
        lowest_temp = temperature_c
        lowest_city= city

    print()
    
    city = input("Please enter the name of a city: ")

    if highest_temp is not None:
      print("\nSummary:")
      print(f"The highest temperature is {highest_temp:.1f} °C in{ highest_city}.")
      print(f"The lowest temperature is {lowest_temp:.1f}°C in{lowest_city}.")

    else:
      print("No temperature were entered.")
