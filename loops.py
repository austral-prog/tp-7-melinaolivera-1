def index_of_by_index(string, lst, start_index):
    try:
        return lst.index(string, start_index)
    except ValueError:
        return -1

def index_of_empty(lst):
    try:
        return lst.index("")
    except ValueError:
        return -1

def index_of(string, lst):
    try:
        return lst.index(string)
    except ValueError:
        return -1

def put(string, lst):
    index = index_of_empty(lst)
    if index != -1:
        lst[index] = string
    return index

def remove(string, lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] == string:
            lst[i] = ""
            count += 1
    return count  # El return debe estar fuera del ciclo para contar todas las ocurrencias

# Pruebas
colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(index_of("Black", colors))  # Debe retornar 3
print(index_of("Blue", colors))   # Debe retornar -1
print(index_of_by_index("Black", colors, 1))  # Debe retornar 3
print(index_of_by_index("Black", colors, 4))  # Debe retornar 6
print(index_of_by_index("Green", colors, 2))  # Debe retornar -1

colors1 = ["Red", "Green", "", "", "Pink", "", "Black"]
colors2 = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(index_of_empty(colors1))  # Debe retornar 2
print(index_of_empty(colors2))  # Debe retornar -1
print(put("Blue", colors1))     # Debe retornar 2 (y colocar "Blue" en el índice 2)
print(remove("Black", colors))  # Debe retornar 2 (ya que hay dos "Black" en la lista)
print(remove("Blue", colors))
