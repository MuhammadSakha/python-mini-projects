def is_pangram(sentence):
    kalimat = sentence.lower()
    alfabet = 'abcdefghijklmnopqrstuvwxyz'

    for huruf in alfabet:
        if huruf not in kalimat:
            return False
    return True