################################
#NOME: Gabriel dos Santos Couto#
#RA: 20.00273-4                #
################################

import sqlite3
from src.models.user import User

class UserDAO:
    _instance = None
    
    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = UserDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db', check_same_thread=False)

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Users;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(name = resultado[1], email = resultado[2], password = resultado[3], cpf = resultado[4]))
        self.cursor.close()
        return resultados

    def inserir_user(self, user):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Users(name, email, password, cpf)
            Values(?,?,?,?);
        """, (user.get_name(), user.get_email(), user.get_password(),user.get_cpf()))
        self.conn.commit()
        self.cursor.close()

    def pegar_user(self, email):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Users
            WHERE email = '{email}';
        """)
        user  = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            user = (User(name = resultado[1], email = resultado[2], password = resultado[3], cpf = resultado[4]))
        self.cursor.close()
        return user

    def atualizar_user(self, user):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Users SET
                email = '{user.get_email()}',
                password = '{user.get_password()}'
                WHERE cpf = '{user.get_cpf()}'
                
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def deletar_user(self, email):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Users 
                WHERE email = '{email}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def search_all_for_name(self, name):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Users
            WHERE name LIKE '{name}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(name = resultado[1], email = resultado[2], password = resultado[3], cpf = resultado[4]))
        self.cursor.close()
        return resultados