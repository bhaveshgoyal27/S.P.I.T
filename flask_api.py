from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import spacy
import requests
import json

app = Flask(__name__)
api = Api(app)

nlp = spacy.load('en_core_web_sm')

def details(name):
	response = requests.get(url="http://dataservice.accuweather.com/locations/v1/search?apikey=vcI1i8BQsPiJh5ObbwIlTFSEDmlRY8Vd&amp&q="+name)
	print(response.status_code)
	response_json = json.loads(response.content)
	a = response_json[0]['Key']

	url = f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/{a}?apikey=vcI1i8BQsPiJh5ObbwIlTFSEDmlRY8Vd&amp&details=true&amp"
	response = requests.get(url=url)
	json_data = json.loads(response.content)
	print(f"5-day summery: {json_data['Headline']['Text']}")
	f={}
	i=1
	for d in json_data["DailyForecasts"]:
		e={}
		e["Min temperature"]=str(d['Temperature']['Minimum']['Value'])+str(d['Temperature']['Minimum']['Unit'])
		e["Max temperature"]=str(d['Temperature']['Maximum']['Value'])+str(d['Temperature']['Maximum']['Unit'])
		e["Description"] = d['Day']['LongPhrase']
		e["Rain probability"] = str(d['Day']['RainProbability'])+"%"
		e["Wind Speed"] = str(d['Day']['Wind']['Speed']['Value'])+ str(d['Day']['Wind']['Speed']['Unit'])
		f[str(i)]=e
		i+=1
	f['city']=name
	data={'data':f}
	return data
		# print(f"Min temperature: {d['Temperature']['Minimum']['Value']} {d['Temperature']['Minimum']['Unit']}")
		# print(f"Max temperature: {d['Temperature']['Maximum']['Value']} {d['Temperature']['Maximum']['Unit']}")
		# print(f"Description: {d['Day']['LongPhrase']}")
		#print(f"Rain probability: {d['Day']['RainProbability']} %")
		#print(f"Wind speed: {d['Day']['Wind']['Speed']['Value']} {d['Day']['Wind']['Speed']['Unit']}")

parser = reqparse.RequestParser()
parser.add_argument('query')

class Predict(Resource):
    def post(self):
        args = parser.parse_args()
        msg = args['query']
        doc = nlp(msg)
        result={}
        for ent in doc.ents:
            if ent.label_=="GPE" or ent.label_=="ORG":
                result = details(ent.text)
        return result

api.add_resource(Predict, '/')