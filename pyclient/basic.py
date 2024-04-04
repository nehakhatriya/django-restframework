import requests

endpoint = 'http://localhost:8000/api/'

# get_response=requests.get(endpoint)
post_response=requests.post(endpoint, params={'abc':123}, json={'title':'replace this'})
# print(get_response.json())
print(post_response.json())