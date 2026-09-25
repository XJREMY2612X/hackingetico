# 2. Solo correos electrónicos[cite: 11]
usuarios = [
    {"name": "Juan", "email": "juan@test.com"},
    {"name": "Sara", "email": "sara@test.com"}
]

emails = [u["email"] for u in usuarios if "email" in u]
print("Emails:", emails)
