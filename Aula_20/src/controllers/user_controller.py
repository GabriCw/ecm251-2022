from models.user import User

class UserController():
    def __init__(self) -> None:
        #carrega os dados dos usuarios
        self.users = [
            User(name="joao", password="arroz", email="joao@gmail.com"),
            User(name="joao2", password="arroz2", email="joao@amaaroz.com"),
            User(name="tais", password="petacular", email="tais_@amaaroz.com")
        ]
    
    def checkUser(self, user):
        return user in self.users

    def checkLogin(self, name, password):
        user_teste = User(name=name, password=password, email=None)
        for user in self.users:
            if user.name == user_teste.name and user.password == user_teste.password:
                return True
        return False