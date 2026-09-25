# 3. Buscar por correo electrónico[cite: 11]
def find_user_by_email(users, email):
    return next((u for u in users if u.get("email") == email), None)
