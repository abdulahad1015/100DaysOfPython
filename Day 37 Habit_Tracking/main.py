import requests
from datetime import *
TOKEN = "y1hh1sr1421966hwpsm"
date=datetime.now()
pixela_endpoint = f"https://pixe.la/v1/users/abdulahad1015/graphs/graph1"



user_params = {
    "token": "y1hh1sr1421966hwpsm",
    "username": "abdulahad1015",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
graph_config = {
    "id": "graph1",
    "name": "Commit Graph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_post={
    "date":date.strftime("%Y%m%d"),
    "quantity":"1",
}


response = requests.post(url=pixela_endpoint, json=pixel_post,headers=headers)

print(response.text)
