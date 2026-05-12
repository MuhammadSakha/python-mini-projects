def response(hey_bob):

    pesan = hey_bob.strip()

    if not pesan:
        return "Fine. Be that way!"

    is_yelling = pesan.isupper()
    is_question = pesan.endswith('?')
    
    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question :
        return "Sure."
    else:
        return "Whatever."