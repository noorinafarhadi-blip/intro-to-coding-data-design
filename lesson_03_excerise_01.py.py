city = input("Please enter the name of the city: ")
while city.lower() != "exit":

        temperature_f = float(input(
                f"Please enter the current temperaturein Fahrenheit in{city}: "
        ))

        temperature_c =(temperature_f - 32) * 5./ 9

        print (
             f"The current temeprature in {city} is "   
             f"{temperature_f} °F or {temperature_c:.1f}°C."
        )
        if temperature_c < 0:
                print("Warning: The temperature is below reezing point.")

                city= input("\nPleae enter the name of the a city: " )

        print("Progam finished") 