def delete(list_, index = None):
    if index == None:
        return "введите индекс :("
    elif index < 0:
        return "индекс отрицаетельный!"
    else:
        left = list_[:index]
        right = list_[index + 1:]
        list_ = left + right
    return list_


print(delete([0, 0, 1, 2], index = 0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index = 1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]

print("\n")
# или так нужно?

def delete(list_, index = None):
    if index == None:
        return list_
    elif index < 0:
        left = list_[:index]
        if index == -1:
            list_ = left
            return list_
        else:
            right = list_[index + 1:]
            list_ = left + right
            return list_
    else:
        left = list_[:index]
        right = list_[index + 1:]
        list_ = left + right
    return list_


print(delete([0, 0, 1, 2], index = 0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index = 1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
