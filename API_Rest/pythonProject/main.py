from MySQLdb import connect
from flask import Flask, jsonify, request, render_template
from flask_pydantic_spec import FlaskPydanticSpec, Request, Response
from pydantic import BaseModel, Field
from typing import List, Optional
# Biblioteca utilizada: mysql-connector-python
from time import sleep

connection = connect(host="localhost", user="root", password="1234", database="bd_teste")
cursor = connection.cursor()
cursor.execute(
    "create table if not exists usuarios (idUser int auto_increment primary key, Nome_usu varchar(50), email varchar(50), senha varchar(50), idade int default 0)")
app = Flask(__name__)

spec = FlaskPydanticSpec("flask", title="Teste online")
spec.register(app)


class Pessoa(BaseModel):
    nome: str
    email: str
    senha: str
    idade: int


@app.route('/')
def homepage():
    return render_template('index.html', Marca="Rafael")

@app.route('/cadastrar')
def Cadastra_page():
    return render_template('cadastrar.html', Marca="Rafael")

@app.route('/cadastrar/processar', methods=['POST'])
def processar():
    try:
        # Adicione depuração para verificar os dados recebidos
        # print(request.form)
        nome_usu = request.form.get('nome')
        email_usu = request.form.get('email')
        senha_usu = request.form.get('senha')
        idade = request.form.get('idade')

        if not nome_usu or not email_usu or not senha_usu or not idade:
            return jsonify({'error': 'Dados incompletos'}), 400
        nome_usu = nome_usu.strip().title().replace(' ', '_').replace("'", "").replace(")", "").replace("(", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "").replace("/", "").replace("=", "").replace("+", "").replace("-", "").replace("*", "").replace("&", "").replace("%", "").replace("$", "").replace("#", "").replace("@", "").replace("--", "")
        email_usu = email_usu.strip().replace(' ', '_').replace("'", "").replace(")", "").replace("(", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "").replace("/", "").replace("=", "").replace("+", "").replace("-", "").replace("*", "").replace("&", "").replace("%", "").replace("$", "").replace("#", "").replace("--", "")
        senha_usu = senha_usu.strip().replace("'", "").replace(")", "").replace("(", "").replace(",", "").replace(".", "").replace(":", "").replace(";", "").replace("/", "").replace("=", "").replace("+", "").replace("-", "").replace("*", "").replace("&", "").replace("%", "").replace("$", "").replace("#", "").replace("--", "")
        cursor.execute(f"insert into usuarios (Nome_usu, email, senha, idade) values ('{nome_usu}', '{email_usu}', '{senha_usu}', '{request.form.get('idade')}')")
        connection.commit()
        return jsonify({'message': f'Nome: {nome_usu}, Email: {email_usu}, Senha: {senha_usu}, Idade: {request.form.get('idade')}'})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.get('/cadastro')  # Puxando os dados do banco de dados e colocando na API
@spec.validate(resp=Response())
def cadastro():
    resultado_format = {}
    cursor.execute('select * from usuarios')
    resultado = cursor.fetchall()
    for linha in resultado:
        resultado_format[linha[0]] = {"nome": linha[1], "email": linha[2], "senha": linha[3], "idade": linha[4]}

    return jsonify(resultado_format)


@app.post('/cadastro')  # Colocando novos dados no banco de dados e na API
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_200=Pessoa))
def post_usu():
    body = request.context.body.dict()
    nome_usu = body["nome"].strip().title().replace(' ', '_').replace("'", "").replace(")", "").replace("(",
                                                                                                        "").replace(",",
                                                                                                                    "").replace(
        ".", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "").replace("/", "").replace("=",
                                                                                                              "").replace(
        "+", "").replace("-", "").replace("*", "").replace("&", "").replace("%", "").replace("$", "").replace("#",
                                                                                                              "").replace(
        "@", "").replace("--", "")
    email_usu = body["email"].strip().replace(' ', '_').replace("'", "").replace(")", "").replace("(",
                                                                                                  "").replace(
        ",", "").replace(".", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "").replace("/",
                                                                                                              "").replace(
        "=", "").replace("+", "").replace("-", "").replace("*", "").replace("&", "").replace("%", "").replace("$",
                                                                                                              "").replace(
        "#", "").replace("--", "")
    senha_usu = body["senha"].strip().replace("'", "").replace(")", "").replace("(", "").replace(",",
                                                                                                 "").replace(
        ".", "").replace(":", "").replace(";", "").replace("/", "").replace("=", "").replace("+", "").replace("-",
                                                                                                              "").replace(
        "*", "").replace("&", "").replace("%", "").replace("$", "").replace("#", "").replace("--", "")
    cursor.execute(f"insert into usuarios (Nome_usu, email, senha) values ('{nome_usu}', '{email_usu}', '{senha_usu}', '{body['idade']}')")
    connection.commit()
    return jsonify(body)


@app.put('/cadastro/<int:id>')  # Substituindo dados no banco de dados e na API
@spec.validate(body=Request(Pessoa), resp=Response())
def altera_usuario(id: int):
    body = request.context.body.dict()
    nome_usu = body["nome"].strip().title().replace(' ', '_').replace("'", "").replace(")", "").replace("(",
                                                                                                        "").replace(
        ",", "").replace(".", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "").replace("/",
                                                                                                              "").replace(
        "=", "").replace("+", "").replace("-", "").replace("*", "").replace("&", "").replace("%", "").replace("$",
                                                                                                              "").replace(
        "#", "").replace("@", "")
    email_usu = body["email"].strip().replace(' ', '_').replace("'", "").replace(")", "").replace("(",
                                                                                                  "").replace(
        ",", "").replace(".", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "").replace("/",
                                                                                                              "").replace(
        "=", "").replace("+", "").replace("-", "").replace("*", "").replace("&", "").replace("%", "").replace("$",
                                                                                                              "").replace(
        "#", "").replace("--", "")
    senha_usu = body["senha"].strip().replace("'", "").replace(")", "").replace("(", "").replace(",",
                                                                                                 "").replace(
        ".", "").replace(":", "").replace(";", "").replace("/", "").replace("=", "").replace("+", "").replace("-",
                                                                                                              "").replace(
        "*", "").replace("&", "").replace("%", "").replace("$", "").replace("#", "").replace("--", "")
    cursor.execute(
        f"update usuarios set Nome_usu = '{nome_usu}', email = '{email_usu}', senha = '{senha_usu}' where idUser = {id}")
    connection.commit()
    return jsonify(body)


@app.get('/cadastro/<int:id>')  # Procurando dados no banco de dados e na API via ID
@spec.validate(resp=Response())
def procura_id(id: int):
    resultado_format = {}
    cursor.execute(f'select * from usuarios where idUser = {id}')
    resultado = cursor.fetchall()
    for linha in resultado:
        resultado_format[linha[0]] = {"nome": linha[1], "email": linha[2], "senha": linha[3]}

    return jsonify(resultado_format)


@app.delete('/cadastro/<int:id>')  # Deletando dados no banco de dados e na API via ID
@spec.validate(resp=Response())
def deleta_id(id: int):

    cursor.execute(f'select * from usuarios where idUser = {id}')
    resultado = cursor.fetchall()[0]
    cursor.execute(f'delete from usuarios where idUser = {id}')
    connection.commit()
    return f"Usuário com os dados: ID: {resultado[0]}, Nome: {resultado[1]} e Email: {resultado[2]} foi deletado com sucesso!"


if __name__ == '__main__':
    app.run(debug=True)