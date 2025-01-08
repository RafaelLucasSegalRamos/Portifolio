from MySQLdb import connect # Biblioteca utilizada: mysql-connector-python


def listar_Clientes(con):
    connection = connect(host=con["host"], user=con["user"], password=con["password"], database=con["database"])
    cursor = connection.cursor()
    cursor.execute("select * from usuarios")
    tudo = cursor.fetchall()
    # print(tudo)
    
    texto = '''<table>\n
            <tr>\n
                <th>ID</th>\n
                <th>Nome</th>\n
                <th>Email</th>\n
                <th>Senha</th>\n
                <th>Idade</th>\n
            </tr>\n'''
    for i in tudo:
        texto += '<tr>\n'
        for pos, j in enumerate(i):
            texto += f'<td>{j}</td> \n'
        texto += '</tr>\n'
    texto += "</table>"
    return texto

    