d_symb_freq = {}

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

def get_count_char(str_):
    newstr = str_.lower().replace(" ", "")
    str_length = len(newstr)
    for i in newstr:
        if i.isalpha():
            d_symb_freq[i] = d_symb_freq.get(i, 0) + 1
    return d_symb_freq
print("1. словарь с частотой каждого символа:\n", get_count_char(main_str))


def get_percent(dict_):
    sum_ = sum(dict_.values())
    for k, v in dict_.items():
        dict_[k] = round((v * 100)/sum_, 3)
    return dict_

print("2. словарь с процентным соотношением:\n", get_percent(d_symb_freq))
