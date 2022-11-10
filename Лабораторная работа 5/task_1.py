# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
def list_of_dict(n):
    return [{"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)} for i in range(n+1)]
pprint(list_of_dict(15))