import requests
endpoint="http://127.0.0.1:8000/"
get_response=requests.get(endpoint,params={"product_id":"4"})
print(get_response.text)
print(get_response.json())



