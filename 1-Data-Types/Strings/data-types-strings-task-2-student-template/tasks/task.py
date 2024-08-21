def get_longest_word(s: str) -> str:
    longest_word = ''
    for word in s.split():
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word
