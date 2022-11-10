from typing import List
import random
def get_unique_list_numbers() -> List[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    random_list = [i for i in range(-10, 10)]
    random.shuffle(random_list)
    return random_list[:15]

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
