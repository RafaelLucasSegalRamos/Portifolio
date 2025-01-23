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
    for pos, i in enumerate(ret):
        texto += '<tr>\n'
        for pos, j in enumerate(i):
            texto += f'<td>{j}</td> \n'
            if pos == 0:
                id = j
        texto += f'<td><a><button onclick="deletar({id});">Deletar</button></a></td>\n'
        texto += f'<td><a><button onclick="alterar({id});">Alterar</button></a></td>\n'
        texto += '</tr>\n'
    texto += "</table>"
    return texto
