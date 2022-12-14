def my_split(text):
    word = ""
    result = []
    for character in text:
        if character != " ":
            word = word + character
        elif character == " " and word != "":
            result.append(word)
            word = ""
    if word != "":
        result.append(word)
    return result
