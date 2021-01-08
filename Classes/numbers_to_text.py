def numbers_to_text(number):
    number = int(number)
    if 10 ** 9 > number >= 10 ** 6:
        value = '{0:.3f}'.format(number / 10 ** 6)
        return f'{value}mill'
    elif number >= 10 ** 9:
        value = '{0:.3f}'.format(number / 10 ** 9)
        return f'{value}bill'
    return number
