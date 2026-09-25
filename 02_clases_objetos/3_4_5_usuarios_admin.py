# 3, 4 y 5. Herencia, Lista de objetos y Conteo de instancias[cite: 10]
class User:
    # Contador a nivel de clase
    user_count = 0 
    
    def __init__(self, username):
        self.username = username
        User.user_count += 1
        
    def display(self):
        print(f"Usuario: {self.username}")

class Admin(User):
    def __init__(self, username):
        super().__init__(username)
        self.role = 'admin'
        
    def display(self):
        print(f"Usuario: {self.username} | Rol: {self.role}")

# Lista de objetos e iteración
usuarios = [User("juan"), Admin("root_admin"), User("maria")]
for u in usuarios:
    u.display()

print(f"Total de instancias creadas: {User.user_count}")
