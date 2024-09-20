def vigenere_encrypt(plaintext, key):
    encrypted = []
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = (ord(char.upper()) + ord(key[key_index]) - 2 * ord('A')) % 26
            encrypted.append(chr(shift + ord('A')))
            key_index = (key_index + 1) % key_length
        else:
            encrypted.append(char)
    return ''.join(encrypted)

def vigenere_decrypt(ciphertext, key):
    decrypted = []
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = (ord(char.upper()) - ord(key[key_index]) + 26) % 26
            decrypted.append(chr(shift + ord('A')))
            key_index = (key_index + 1) % key_length
        else:
            decrypted.append(char)
    return ''.join(decrypted)
