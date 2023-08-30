import requests

endpoint="http://127.0.0.1:8000/products/13/destroy/"
get_response=requests.delete(endpoint)
print(get_response)



