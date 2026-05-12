def convert(number):

    aturan = [(3, "Pling"), (5, "Plang"), (7, "Plong")]

    hasil = "".join(kata for div, kata in aturan if number % div == 0)

    return hasil or str(number)