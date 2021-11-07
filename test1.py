import requests
import json

response = requests.get(url="http://dataservice.accuweather.com/forecasts/v1/daily/1day/268068?apikey=LjCmfhvAv5mVnWQAgQ5xGOLTCFqhGCEh")
print(response.status_code)
response_json = json.loads(response.content)
print(response_json["Headline"]["Text"])
min_temperature = response_json["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]
print(f"Minimum Temperature: {min_temperature}")
max_temperature = response_json["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]
print(f"Maximum Temperature: {max_temperature}")
min_temperature = str(response_json["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]) + response_json["DailyForecasts"][0]["Temperature"]["Minimum"]["Unit"]
print(f"Minimum Temperature: {min_temperature}")

max_temperature = str(response_json["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]) + response_json["DailyForecasts"][0]["Temperature"]["Maximum"]["Unit"]
print(f"Maximum Temperature: {max_temperature}")