import requests
import json    

BASE_URL = 'https://reqres.in'

def test_list_user():
     response = requests.get(BASE_URL +"/api/users?",{'page':2})
     bodyResponse = response.content
     print(bodyResponse)
     response_body = response.json()
     assert response.status_code == 200
     assert response_body["data"][1]["email"] == "lindsay.ferguson@reqres.in"

def test_create_user():
     response = requests.post(BASE_URL +"/api/users",{"name": "morpheus","job": "leader"})
     bodyResponse = response.content
     a = json.loads(bodyResponse)
     print(bodyResponse)
     response_body = response.json()
     assert response.status_code == 201
     # print(response_body)
     ResponseId = a["id"]
     ResponseJob = a["job"]
     print('Response Id : '+ResponseId)
     print('Response Job : '+ResponseJob)