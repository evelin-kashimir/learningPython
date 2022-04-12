import mysql.connector

con = mysql.connector.connect(host='localhost', database='dbBanco', user='root', password='kashinho123')

if con.is_connected():
    db_info = con.get_server_info()
    print('Conectado ao servidor.', db_info)


# class Conexao():
#     def __init__(self,host,banco,usuario,senha):
#         self.host = host
#         self.banco = banco
#         self.usuario = usuario
#         self.senha = senha