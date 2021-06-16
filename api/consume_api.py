import requests
from logic._logic import EmpresaLogic

data = {} #Introduza los datos deseados


""" response = requests.head("http://localhost:23512/") """
""" response = requests.get("http://localhost:23512/") """
""" response = requests.post("http://localhost:23512/") """
""" response = requests.put("http://localhost:23512/", data=data) """
""" response = requests.patch("http://localhost:23512/", data=data) """
response = requests.delete("http://localhost:23512/")

print(response)
messageJson = response.json()
print(messageJson)