
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

"""
Esta classe será responsável por gerenciar todas as operações relacionadas ao banco de dados, como conexão,
commit, cursor, rollback e fechamento de conexão. Ela utiliza as variáveis de ambiente para obter as credenciais de acesso ao DB
"""
class Database:
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.port = os.getenv('DB_PORT')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = os.getenv('DB_NAME')
        self.connection = None

    #funcao responsavel por estabelecer a coexão com o banco de dados, utilizando as credenciais fornecidas
    #caso já exista uma conexão ativa, ela retorna a conexão ativa, evitando criar conexoes desnecessárias
    def connect(self):
        
        if self.connection is None:
            try:
                self.connection = psycopg2.connect(
                    host = self.host,
                    port = self.port,
                    user = self.user,
                    password = self.password,
                    database = self.database
                )
                return self.connection
            except Exception as error:
                print(f"Erro ao conectar ao Banco de Dados: {error}")
                return None
        else:
            return self.connection
        
    #Funcao responsável por fechar a conexão com o banco de dados
    def close(self) -> None:
        if self.connection is not None:
            try:
                self.connection.close()
                self.connection = None
                return None
            except Exception as error:
                print(f"Erro ao fechar banco de dados: {error}")
                return None
    #função responsavel por permitir as execucoes dos comandos SQL
    def commit(self) -> None:
        if self.connection is not None:
            try:
                self.connection.commit()
                return None
            except Exception as error:
                print(f"Erro ao commitar no banco de dados: {error}")
                return None
    
    #função responsavel por desfazer as operações realizadas no banco de dados, caso ocorra algum erro ou seja necessário reverter alguma ação
    def rollback(self) -> None:
        if self.connection is not None:
            try:
                 self.connection.rollback()
                 return None
            except Exception as error:
                print(f"Erro ao realizar rollback no banco de dados: {error}")
                return None
            
