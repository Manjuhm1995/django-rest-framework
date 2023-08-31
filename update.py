import requests

endpoint="http://127.0.0.1:8000/products/products/19/"
get_response=requests.put(endpoint,data={'title': 'Kasturi Kannada namma kannada',"content":"bhuvaneshwari"})
print(get_response.json())



