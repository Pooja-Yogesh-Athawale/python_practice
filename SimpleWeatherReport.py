import requests
weather = [
    {
        'date':'today',
        'state': 'cloudy',
        'temp': 68.5
    },
    {
        'date':'tomorrow',
        'state': 'sunny',
        'temp': 74.8
    }
]

for forecast in weather:
    # print('The weather for ' + forecast['date'] + ' will be ' + forecast['state'] + ' with a temperature of ' + str(forecast['temp']) + ' degrees.')
#     print(forecast['date'])
#     print(forecast['state'])
#     print(forecast['temp'])
    print(f"The weather for {forecast['date']} will be {forecast['state']} with a temperature of {forecast['temp']} degrees.")
    # for forecast in weather:
    # date = forecast['date']
    # state = forecast['state']
    # temp = forecast['temp']
    # print(f"The weather for {date} will be {state} with a temperature of {temp} degrees.")