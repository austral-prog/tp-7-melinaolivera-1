def index_of(target, strings):
    for i, s in enumerate(strings):
        if s == target:
            return i
    return -1  


def index_of_by_index(target, strings, start_index):
    for i in range(start_index, len(strings)):
        if strings[i] == target:
            return i
    return -1  

def index_of_empty(strings):
    for i, s in enumerate(strings):
        if s == "":
            return i
    return -1  


def put(target, strings):
    empty_index = index_of_empty(strings)
    if empty_index != -1:
        strings[empty_index] = target
    return empty_index 


def remove(target, strings):
    count = 0
    for i, s in enumerate(strings):
        if s == target:
            strings[i] = ""
            count += 1
    return count  


colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]


print(index_of("Black", colors))  
print(index_of("Blue", colors))   


print(index_of_by_index("Black", colors, 1))  
print(index_of_by_index("Black", colors, 4))  
print(index_of_by_index("Green", colors, 2))  

print(index_of_empty(colors))  

colors_with_empty = ["Red", "Green", "", "", "Pink", "", "Black"]
print(index_of_empty(colors_with_empty))  


print(put("Blue", colors_with_empty))  
print(put("Blue", colors))  
