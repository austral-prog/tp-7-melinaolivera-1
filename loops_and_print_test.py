import unittest.mock

import loops_and_print as ex1


class TP7LoopsAndPrintTest(unittest.TestCase):

    
def enumerate_list(strings):
    result = []
    for index, value in enumerate(strings):
        if value:  # Solo agrega si el string no está vacío
            result.append(f"{index}. {value}")
    return result

colors = ["Red", "Green", "", "White", "Black"]
print(enumerate_list(colors))
        
def enumerate_backwards(strings):
    result = []
    for index, value in enumerate(strings):
        if value:
            result.append(f"{index}. {value[ : :-1]}")
    return result
colors = ["Red", "Green", " ", "White", "Black"]
print(enumerate_backwards(colors))
