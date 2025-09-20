import requests
import json  # Import the json module


url = "https://open-weather13.p.rapidapi.com/city"

querystring = {"city":"Atlanta","lang":"EN"}

headers = {
	"x-rapidapi-key": "b21697a4f3mshc18a3118f1a2e72p142c1bjsn2433e369a8a8",
	"x-rapidapi-host": "open-weather13.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

print(json.dumps(response.json(),indent=4))
