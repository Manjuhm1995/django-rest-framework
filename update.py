import requests

endpoint="http://127.0.0.1:8000/products/19/update/"
get_response=requests.put(endpoint,data={"content":"sirigannadam balge"})
print(get_response.json())



