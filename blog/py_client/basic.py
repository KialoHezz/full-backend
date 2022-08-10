import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"

endpoint = "http://localhost:8000/api/"  # http:/127.0.0.1/:8000/



# FOR EXAMPLE pHONE has CAMERA -> App -> API
# REST API -> WEB API  
# API[Application programming interface] -> Method

get_response = requests.get(endpoint,params={"abc": 123} ,json={"query": "Hello Hezron!"}) #HTTP GET request
# print(get_response.text) # print the body or raw TEXT response

# JSON[javascript Object Notation] - > Python Dict
print(get_response.json()) # print the JSON response
