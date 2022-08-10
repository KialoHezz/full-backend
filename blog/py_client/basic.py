import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"



# FOR EXAMPLE pHONE has CAMERA -> App -> API
# REST API -> WEB API  
# API[Application programming interface] -> Method

get_response = requests.get(endpoint, json={"query": "Hello Hezron!"}) #HTTP GET request
print(get_response.text) # print the body or raw TEXT response

# JSON[javascript Object Notation] - > Python Dict
print(get_response.json()) # print the JSON response
