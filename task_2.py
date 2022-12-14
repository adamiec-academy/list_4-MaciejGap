def my_split(text):
    word = ""
    result = []
    for character in text:
        if character != " ":
            word = word + character
        elif character := " ":
            result.append(word)
    return text
