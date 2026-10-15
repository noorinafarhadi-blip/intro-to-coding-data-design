cities = {}
while True:
    city =input("Please enter name of a city: ")
    if city.lower() == "exit" :
        break

    unit= input(
        "Would you like to enter the temperature"
        "in Fahrenheit or Celsius?: "
    ).lower()

    if unit == "celsius" :
        temp_c = float (input(
            f"Please enter the current temperature "
            f"in Celsius in {city} : "
        ))
        temp_f = temp_c * 9/5 + 32

    elif unit == "fahrenheit":
        temp_f = float (input(
            f"Please enter the current temperature "
            f"in Fahrenheit in {city} : "
        ))
        temp_c = (temp_f - 32) * 5/ 9

    else:
        print("Invalid unit. Please try again.")
        continue
    raining = input(
        f"Is it raining in {city}? (yes/no): "
    ).lower()

    sunny = input(
        f"Is the sun shining in {city}? (yes/no)"
    ).lower()

    cities[city] = {
        "celsius": temp_c,
        "fahrenheit": temp_f,
        "raining": raining,
        "sunny": sunny
    }

    print("\nSummary:")

    for city, weather in cities.items():

        temp_c =weather["celsius"]
        temp_f =weather["fahrenheit"]
        raining =weather["raining"]
        sunny =weather["sunny"]

        print(f"\n{city}:")
        print(f"Temperature:{temp_c:.1f}°C, {temp_f:.1f} °F")

        if raining == "yes":
            print("It is raining.")


        else:
            print("It is not raining.")
        if sunny == "yes":
            print("It is sunny")
        else:
            print("It is not sunny")

        if temp_c < 0:
            print("WARNING: The temperature is below 0°C!")

        if raining == "yes" and sunny == "yes":
            print("There is a rainbow!")