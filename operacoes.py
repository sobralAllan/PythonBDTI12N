import mysql.connector
import conexao

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def inserir(nome, telefone, endereco, dataAtual):
    try:
        dataAtual = transformarData(dataAtual)
        sql = "insert into pessoa(codigo, nome, telefone, endereco, dataAtual) values('','{}','{}','{}','{}')".format(nome, telefone, endereco, dataAtual)
        con.execute(sql)#Prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
        print(con.rowcount, "Inserido!")
    except Exception as erro:
        print(erro)

#Consultar os dados do BD
def selecionar():
    try:
        sql = "select * from pessoa"
        con.execute(sql)

        for (codigo, nome, telefone, endereco, dataAtual) in con:
            print(codigo, nome, telefone, endereco, dataAtual)
        print('\n')
    except Exception as erro:
        print(erro)

#Atualizar dados no banco de dados
def atualizarNome(codigo, nome):
    try:
        sql = "update pessoa set nome = '{}' where codigo = '{}'".format(nome,codigo)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def atualizarTelefone(codigo, telefone):
    try:
        sql = "update pessoa set telefone = '{}' where codigo = '{}'".format(telefone,codigo)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def atualizarEndereco(codigo, endereco):
    try:
        sql = "update pessoa set endereco = '{}' where codigo = '{}'".format(endereco,codigo)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def atualizarData(codigo, dataAtual):
    try:
        dataAtual = transformarData(dataAtual)
        sql = "update pessoa set dataAtual = '{}' where codigo = '{}'".format(dataAtual,codigo)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def excluir(codigo):
    try:
        sql = "delete from pessoa where codigo = '{}'".format(codigo)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Deletada!")
    except Exception as erro:
        print(erro)

def transformarData(texto):
    separado = texto.split('/')
    dia = separado[0]
    mes = separado[1]
    ano = separado[2]
    return '{}-{}-{}'.format(ano,mes,dia)