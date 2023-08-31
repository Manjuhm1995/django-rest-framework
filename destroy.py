import requests

endpoint="http://127.0.0.1:8000/products/products/19/"
get_response=requests.delete(endpoint)
print(get_response)



