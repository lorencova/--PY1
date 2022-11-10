import random, string
def get_random_password(n) -> str:
    ...  # TODO написать функцию генерации случайных паролей
    allowed_alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = ''.join(random.sample(allowed_alphabet, k = n))
    return password
print(get_random_password(8))
