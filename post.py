import requests
endpoint="http://127.0.0.1:8000/products/products/"
get_response=requests.post(endpoint,data={"title":"Kasturi Kannada namma kannada","price":"100"})
print(get_response.json())



