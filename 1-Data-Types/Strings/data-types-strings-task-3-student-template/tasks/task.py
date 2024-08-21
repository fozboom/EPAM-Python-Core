def replacer(s: str) -> str:
    temp_char = '\0'
    s = s.replace("'", temp_char)
    s = s.replace('"', "'")
    s = s.replace(temp_char, '"')
    return s
