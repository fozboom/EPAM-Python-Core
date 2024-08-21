class Cipher:
    def __init__(self, keyword):
        self.keyword = keyword.upper()
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.cipher_alphabet = self.generate_cipher_alphabet()

    def generate_cipher_alphabet(self):
        keyword_no_duplicates = ''
        for char in self.keyword:
            if char not in keyword_no_duplicates:
                keyword_no_duplicates += char
        remaining_alphabet = ''.join([char for char in self.alphabet if char not in keyword_no_duplicates])
        return keyword_no_duplicates + remaining_alphabet

    def encode(self, plaintext):
        plaintext = plaintext.upper()
        encoded_text = ''
        for char in plaintext:
            if char in self.alphabet:
                encoded_text += self.cipher_alphabet[self.alphabet.index(char)]
            else:
                encoded_text += char
        return encoded_text.capitalize()

    def decode(self, ciphertext):
        ciphertext = ciphertext.upper()
        decoded_text = ''
        for char in ciphertext:
            if char in self.cipher_alphabet:
                decoded_text += self.alphabet[self.cipher_alphabet.index(char)]
            else:
                decoded_text += char
        return decoded_text.capitalize()
