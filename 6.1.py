class UserAccount:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        if self.__password == password:
            return True
        else:
            return False



Kesha = UserAccount('Kyrlik', 'frfrfr', 'babadook228')
Kesha.set_password('lololoshka')
print(Kesha.check_password('lololoshka'))
print(Kesha.check_password('frfrfr'))



