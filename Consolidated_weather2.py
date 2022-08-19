import requests

r = requests.get('https://www.metaweather.com/api/location/2455920')
d = r.json()

print(d['consolidated_weather'][0]['applicable_date'])
print(d['consolidated_weather'][0]['humidity'])
print(d['consolidated_weather'][1]['applicable_date'])
print(d['consolidated_weather'][1]['humidity'])
print(d['consolidated_weather'][2]['applicable_date'])
print(d['consolidated_weather'][2]['humidity'])
print(d['consolidated_weather'][3]['applicable_date'])
print(d['consolidated_weather'][3]['humidity'])
print(d['consolidated_weather'][4]['applicable_date'])
print(d['consolidated_weather'][4]['humidity'])
print(d['consolidated_weather'][5]['applicable_date'])
print(d['consolidated_weather'][5]['humidity'])

# for forecast in d['consolidated_weather']:
#     date = forecast['applicable_date']
#     humidity = forecast['humidity']
#     print(f"{date}\tHumidity: {humidity}")