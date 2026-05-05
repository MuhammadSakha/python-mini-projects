def is_armstrong_number(number):

    str_num = str(number)
    n = len(str_num)

    total = sum(int(digit)**n for digit in str_num)

    return total == number
