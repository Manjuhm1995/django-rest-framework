import requests
endpoint="http://127.0.0.1:8000/"
get_response=requests.post(endpoint,data={"title":"sirigannadam gelge","price":"150"})
print(get_response.text)
print(get_response.json())



