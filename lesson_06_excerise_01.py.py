import requests

# Dictionary with weather codes and descriptions
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    77: "Snow grains",
    80: "Slight rain shower",
    81: "Moderate rain shower",
    82: "Violent rain shower",
    85: "Slight snow shower",
    86: "Heavy snow shower",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


def get_coordinates(city_name):
    """Returns latitude, longitude and elevation."""
    url = (
        "https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city_name}&count=1&language=en&format=json"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    if not data.get("results"):
        raise Exception("City not found.")

    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]
    elevation = data["results"][0]["elevation"]

    return latitude, longitude, elevation


def get_weather(city_name):
    # Get the coordinates of the city
    try:
        latitude, longitude, elevation = get_coordinates(city_name)
    except Exception as e:
        print(e)
        return "Error", float("nan")

    # Create the weather API URL
    url = "https://api.open-meteo.com/v1/forecast?"
    url += "current_weather=true"
    url += f"&latitude={latitude}"
    url += f"&longitude={longitude}"
    url += f"&elevation={elevation}"

    # Send the request and get the response
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Convert JSON into a Python dictionary
        data = response.json()

        # Get temperature and weather code
        temperature = data["current_weather"]["temperature"]
        weather_code = data["current_weather"]["weathercode"]

        # Get weather description from the dictionary
        weather = WEATHER_CODES.get(
            weather_code, "Unknown weather"
        )

        return weather, temperature

    except (requests.RequestException, KeyError, ValueError) as e:
        print("Could not get weather data:", e)
        return "Error", float("nan")


if __name__ == "__main__":
    # Keep asking for a city until the user types exit
    while True:
        city_name = input(
            "Please enter the name of a city: "
        ).strip()

        # Stop the program if the user types exit
        if city_name.lower() == "exit":
            print("Goodbye!")
            break

        # Get weather and temperature
        weather, temperature = get_weather(city_name)

        # Print the result
        if weather != "Error":
            print(
                f"The current weather in {city_name} is "
                f"{weather} and the temperature is "
                f"{temperature}°C."
            )

