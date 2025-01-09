from MySQLdb import connect  # Biblioteca utilizada: mysql-connector-python


def listar_Clientes(ret):
    texto = '''<table>\n
            <tr>\n
                <th>ID</th>\n
                <th>Nome</th>\n
                <th>Email</th>\n
                <th>Senha</th>\n
                <th>Idade</th>\n
            </tr>\n'''
    for i in ret:
        texto += '<tr>\n'
        for pos, j in enumerate(i):
            texto += f'<td>{j}</td> \n'
        texto += '</tr>\n'
    texto += "</table>"
    return texto
