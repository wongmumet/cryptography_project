def create_playfair_matrix(key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    key = key.replace('J', 'I')
    
    matrix = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    for char in key:
        if char not in matrix and char in alphabet:
            matrix.append(char)
    
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    return matrix

def playfair_encrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    plaintext = plaintext.replace('J', 'I').upper()
    plaintext = ''.join(filter(str.isalpha, plaintext))

    ciphertext = ''
    
    pairs = []
    i = 0
    while i < len(plaintext):
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            pairs.append(plaintext[i] + 'X')
            i += 1
        else:
            pairs.append(plaintext[i] + (plaintext[i + 1] if i + 1 < len(plaintext) else 'X'))
            i += 2

    for a, b in pairs:
        row_a, col_a = divmod(matrix.index(a), 5)
        row_b, col_b = divmod(matrix.index(b), 5)

        if row_a == row_b:  # Same row
            ciphertext += matrix[row_a * 5 + (col_a + 1) % 5]
            ciphertext += matrix[row_b * 5 + (col_b + 1) % 5]
        elif col_a == col_b:  # Same column
            ciphertext += matrix[((row_a + 1) % 5) * 5 + col_a]
            ciphertext += matrix[((row_b + 1) % 5) * 5 + col_b]
        else:  # Rectangle
            ciphertext += matrix[row_a * 5 + col_b]
            ciphertext += matrix[row_b * 5 + col_a]

    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = create_playfair_matrix(key)
    plaintext = ''
    
    pairs = []
    i = 0
    while i < len(ciphertext):
        pairs.append(ciphertext[i:i+2])
        i += 2

    for a, b in pairs:
        row_a, col_a = divmod(matrix.index(a), 5)
        row_b, col_b = divmod(matrix.index(b), 5)

        if row_a == row_b:  # Same row
            plaintext += matrix[row_a * 5 + (col_a - 1) % 5]
            plaintext += matrix[row_b * 5 + (col_b - 1) % 5]
        elif col_a == col_b:  # Same column
            plaintext += matrix[((row_a - 1) % 5) * 5 + col_a]
            plaintext += matrix[((row_b - 1) % 5) * 5 + col_b]
        else:  # Rectangle
            plaintext += matrix[row_a * 5 + col_b]
            plaintext += matrix[row_b * 5 + col_a]

    plaintext = plaintext.replace('X', '').replace('I', 'J')
    
    return plaintext
