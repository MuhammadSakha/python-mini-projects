def rotate(text, key):
    
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""

    for karakter in text:
        
        kapital = karakter.isupper()
        nonkapital = karakter.lower()

        if nonkapital in alfabet:
        
            indeks_sekarang = 0
        
            for i in range(26):
                if alfabet[i] == nonkapital:
                    indeks_sekarang = i
                    break

            indek_baru = (indeks_sekarang + key) % 26
            karakter_baru = alfabet[indek_baru]

            if kapital:
                hasil += karakter_baru.upper()
            else:
                hasil += karakter_baru
        else:
            hasil += karakter
    return hasil
        
