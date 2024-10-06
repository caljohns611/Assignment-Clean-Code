from weather_display import WeatherDisplay


def main():
    display = WeatherDisplay()

    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = display.get_detailed_forecast(city)
        else:
            forecast = display.display_weather(city)
        print(forecast)

if __name__ == "__main__":
    main()