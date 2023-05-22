while True:

    print('Checking Weather condition')


    def determine_weather_condition(temp, humidity):
        if temp >= 30 and humidity > 90:
            print('Hot and humidity')
        elif temp >= 30 and humidity < 90:
            print('Hot')
        elif temp < 30 and humidity >= 90:
            print('Cool And humidity')
        elif temp < 30 and humidity < 90:
            print('Cool')
        else:
            print('Normal')


    temprature = float(input('Enter the Temprature : '))
    Humidity = float(input('Enter the Humidity : '))

    determine_weather_condition(temprature, Humidity)
