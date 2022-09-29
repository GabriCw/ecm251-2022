from models.user import User

class UserController():
    def __init__(self) -> None:

        #Carrega dados do usuário
        self.users = [
            User(name="Gabriel", password="3333"),
            User(name="Couto", password="1234")
        ]
    
    def check_user(self, user):
        return user in self.users
    
    def check_login(self, name, password):
        user_teste = User(name=name, password=password)
        for user in self.users:
            if user.name == user_teste.name and user.password == user_teste.password:
                return True
        return False