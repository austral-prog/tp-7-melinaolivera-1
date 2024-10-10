def enumerate_list(lst):
    result = []
    counter = 0
    for item in lst:
        if item:
            result.append(f"{counter}. {item}")
            counter += 1
    return result


def enumerate_backwards(lst):

    result = []
    counter = 0
    for item in lst:
        if item:
            reversed_item = item[::-1]
            result.append(f"{counter}. {reversed_item}")
            counter += 1
    return result
