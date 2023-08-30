import requests
endpoint="http://127.0.0.1:8000/products/create/"
get_response=requests.post(endpoint,data={"title":"sirigannadam balge","price":"200"})
print(get_response.json())



