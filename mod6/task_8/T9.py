import re
digit_to_letters = {
        '2': '[a|b|c]',
        '3': '[d|e|f]',
        '4': '[g|h|i]',
        '5': '[j|k|l]',
        '6': '[m|n|o]',
        '7': '[p|q|r|s]',
        '8': '[t|u|v]',
        '9': '[w|x|y|z]'
    }


def my_t9(digits):
    pattern="[\n]"
    for digit in str(digits):
        pattern+=f'{digit_to_letters[digit]}'
    return [re.sub(r'\n', '', i) for i in re.findall(pattern+"[\n]",open('words.txt').read().lower())]

print(my_t9(22736368))





print()

