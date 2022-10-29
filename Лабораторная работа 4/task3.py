def delete(list_, index = None):
    del list_[index]
    return list_
print("первый способ:")
print(delete([0, 0, 1, 2], index = 0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index = 1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4], index = 4))  # [0, 1, 2, 3]

def delete(list_, index = None):
    left = list_[:index]
    right = list_[index + 1:]
    list_ = left + right
    return list_
print("второй способ:")
print(delete([0, 0, 1, 2], index = 0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index = 1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4], index = 4))  # [0, 1, 2, 3]
