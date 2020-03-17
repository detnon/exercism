def is_isogram(string):
    if len(string) == 0 :
        return True

    string = string.lower()

    new_string = [string.count(s) for s in string if s.isalpha()]

    for n in new_string:
        if n > 1:
            return False
    return True
