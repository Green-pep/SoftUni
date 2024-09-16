def decrypt_massage(char, n):
        decrypted_letter = ord(char)
        new_letter = chr(decrypted_letter + n)
        return new_letter


key = int(input())
letters_input = int(input())
decrypt_word = ""

for letters in range(0, letters_input):
    letter = input()
    decrypt_word += decrypt_massage(letter, key)

print(decrypt_word)