import requests
import json

response = requests.get(url="http://dataservice.accuweather.com/locations/v1/search?apikey=LjCmfhvAv5mVnWQAgQ5xGOLTCFqhGCEh&amp&q=chennai")
print(response.status_code)
response_json = json.loads(response.content)
a = response_json[0]['Key']

url = f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/{a}?apikey=LjCmfhvAv5mVnWQAgQ5xGOLTCFqhGCEh&amp&details=true&amp"
response = requests.get(url=url)
json_data = json.loads(response.content)
#print(json_data)
print(f"5-day summery: {json_data['Headline']['Text']}")
for d in json_data["DailyForecasts"]:
    print(f"Min temperature: {d['Temperature']['Minimum']['Value']} {d['Temperature']['Minimum']['Unit']}")
    print(f"Max temperature: {d['Temperature']['Maximum']['Value']} {d['Temperature']['Maximum']['Unit']}")
    print(f"Description: {d['Day']['LongPhrase']}")
    print(f"Rain probability: {d['Day']['RainProbability']} %")
    print(f"Wind speed: {d['Day']['Wind']['Speed']['Value']} {d['Day']['Wind']['Speed']['Unit']}")