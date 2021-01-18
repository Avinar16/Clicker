def numbers_to_text(number):
    # converting large numbers
    number = int(number)
    if 10 ** 9 > number >= 10 ** 6:
        value = '{0:.2f}'.format(number / 10 ** 6)
        return f'{value}млн'
    elif number >= 10 ** 9:
        value = '{0:.2f}'.format(number / 10 ** 9)
        return f'{value}млрд'
    elif number >= 10 ** 12:
        return f'>1триллиона'
    return number
