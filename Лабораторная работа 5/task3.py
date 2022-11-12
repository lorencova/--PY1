from typing import List
import random
def get_unique_list_numbers(start, stop, size) -> List[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    random_list = set(random.randint(start, stop) for i in range(size))
    return random_list
list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
