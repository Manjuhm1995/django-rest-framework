import requests

endpoint="http://127.0.0.1:8000/products/6/update/"
get_response=requests.patch(endpoint,data={"content":"sirigannadam balge"})
print(get_response.json())



