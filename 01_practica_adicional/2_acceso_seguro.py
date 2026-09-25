# 2. Acceso seguro a listas[cite: 9]
def get_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None
