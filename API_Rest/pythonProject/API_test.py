import requests

url = "http://127.0.0.1:5000/cadastro"

result = requests.get(url)

for k, i in result.json().items():
    print(f'ID: {k} | Nome: {i["nome"]} | Email: {i["email"]} | Senha: {i["senha"]} | Idade: {i["idade"]}')