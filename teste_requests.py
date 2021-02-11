import requests


#  Get provas

provas = requests.get('http://localhost:8000/api/v2/gabarito')

# acessando o status http

print(provas.status_code)

# Acessando os dados da resposta

print(provas.json())

# Acessando a quantidade de registros

print(provas.json()['count'])

# Acessando os resultados

print(provas.json()['results'])

# Acessando o primeiro elemento da lista de resultados

print(provas.json()['results'][-1])

# Acessando somente a prova do resultado especifico

print(provas.json()['results'][-1]['gabarito'])
