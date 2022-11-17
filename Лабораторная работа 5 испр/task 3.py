from random import randint
from typing import List

def get_unique_list_numbers(start = -10, stop = 10, size = 15) -> List[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    my_list = []
    while len(my_list) < size:
        numbers = randint(start, stop)
        if numbers not in my_list:
            my_list.append(numbers)
    return my_list
print(get_unique_list_numbers())
print(len(get_unique_list_numbers()) == len(set(get_unique_list_numbers())))
