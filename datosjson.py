import json

with open("myfile.json") as json_file:
    ourjson = json.load(json_file)

token = ourjson.get("token", "No se encontró el token")
expira = ourjson.get("expires_in", "No se encontró la expiración")

print(f"Token: {token}")
print(f"Tiempo restante antes de expiración: {expira} segundos")
<<<<<<< HEAD
 
=======


>>>>>>> Evaluación N°1 DRY7122
