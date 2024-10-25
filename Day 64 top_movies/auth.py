import requests

import requests

name="Harry Potter"

url = f"https://api.themoviedb.org/3/search/movie?query={name}&api_key=f79377b7e617a7bedc2c81b63d391e21&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer f79377b7e617a7bedc2c81b63d391e21"
}

response = requests.get(url, headers=headers)

print(response.text)