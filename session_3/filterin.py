user = list()
user.append({"id":1, "name": "Cesar", "email": "cesar.sinchiguano@gmail.com", "role": "admin"})
user.append({"id":2, "name": "Jeremy", "email": "jeremy.guerrero@gmail.com", "role": "user"})
user.append({"id":3, "name": "Danilo", "email": "danilo@gmail.com", "role": "user"})
user.append({"id":4, "name": "Jorge", "email": "jorge@gmail.com", "role": "admin"})

counter=list()

for u in user:
    if u["role"] == "admin":
        print(f"Name: {u['name']}, Email: {u['email']}, Role: {u['role']}")
        counter.append(u)

print(f"Total Admins: {len(counter)}")


"now as list comprehension"
counter = [u for u in user if u["role"] == "admin"]
print(f"Total Admin Users: {len(counter)}")


"THE USE OF NEXT"
print("the use of next")


finalUser = next((u for u in user if u["id"] == 3), None)
print(finalUser)