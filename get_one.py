import requests
pk=14
endpoint=f"http://127.0.0.1:8000/products/{pk}"
# get_response=requests.get(endpoint,params={"pk":"1"})
get_response=requests.get(endpoint)
print(get_response.json())



