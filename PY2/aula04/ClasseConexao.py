import mysql.connector

class Conexao():
    def __init__(self, host, banco, usuario, senha):
        self.host = host
        self.banco = banco
        self.usuario = usuario
        self.senha = senha
        self.con = mysql.connector.connect(host='localhost', database='dbbanco', user='root', password='kashinho123')

    def select(self,pTabela):
        con = mysql.connector.connect(host='localhost', database='dbbanco', user='root', password='kashinho123')
        if con.is_connected():
            cursor = self.con.cursor()
            sql = 'SELECT * FROM '+ pTabela + ';'
            cursor.execute(sql)
            total = 0
            for linha in cursor:
                total += 1
            if total < 1:
                print(pTabela + ' não possui registros! ')
            else:
                print('Registros da tabela ' + pTabela)
                cursor.execute(sql)
                for reg in cursor:
                    print('Código: ' + str(reg[0]) + '| Número: ' + str(reg[1]) + '| Saldo: ' + str(reg[2]))
                print('Total de registros: ' + str(cursor.rowcount))
        else:
            print('Não está conectando ao banco')

    def insert(self, pTabela):
        con = mysql.connector.connect(host='localhost', database='dbbanco', user='root', password='kashinho123')
        if con.is_connected():
            cursor = self.con.cursor()
            registro_conta = '66995'
            saldo = 5896.9
            sql = 'INSERT INTO ' + pTabela + ' (numero_conta_corrente, saldo_conta_corrente) VALUES ("12345",0)'
            cursor.execute(sql)
            try:
                self.con.commit()
                print('Registros inserido com sucesso')
            except:
                print('Erro ao inserir o registro')
        else:
            print('Não está conectando ao banco')

    def delete(self):
        if self.con.is_connected():
            cursor = self.con.cursor()
            sql = 'DELETE FROM Conta_Corrente WHERE id_conta_corrente = 15'
            cursor.execute(sql)
            try:
                self.con.commit()
                print('Registro excluido com sucesso')
            except:
                print('Erro ao excluir o registro')
        else:
            print('Não está conectando ao banco')

    def update(self):
        if self.con.is_connected():
            cursor = self.con.cursor()
            sql = 'UPDATE Conta_Corrente SET numero_conta_corrente = "54321" WHERE id_conta_corrente = 22'
            cursor.execute(sql)
            try:
                self.con.commit()
                print('Registro alterado com sucesso')
            except:
                print('Erro ao alterar')
        else:
            print('Não está conectando ao banco')

conexao = Conexao('localhost','dbbanco','root','kashinho123')
conexao.select('Conta_Corrente')
conexao.insert('Conta_Corrente')
conexao.delete()
conexao.update()