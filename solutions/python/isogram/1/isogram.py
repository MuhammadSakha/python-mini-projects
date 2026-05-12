def is_isogram(string):

    string = string.lower()

    huruf_pernah_muncul = {}

    for karakter in string:
        
        if not karakter.isalpha():
            continue

        if karakter in huruf_pernah_muncul:
            return False

        huruf_pernah_muncul[karakter] = True

    return True
        