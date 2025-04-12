import json
with open('clientes.json','r') as a:
    clientes = json.load(a)

print(type(clientes))