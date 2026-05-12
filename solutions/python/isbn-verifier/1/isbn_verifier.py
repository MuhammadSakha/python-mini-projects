def is_valid(isbn):

    raw_digits = isbn.replace("-", "")

    if len(raw_digits) != 10:
        return False

    total = 0

    for i in range(10):
        karakter = raw_digits[i]

        pengali = 10 - i

        if i == 9 and karakter == 'X':
            nilai = 10
        elif karakter.isdigit():
            nilai = int(karakter)
        else:
            return False

        total += nilai * pengali

    return total % 11 == 0