def is_palindrome(text):
    text = text.lower()
    text = text.split()
    text = "".join(text)
    if text != text[::-1]:
        return False
    else:
        return True

