def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").upper()
    n = len(key_matrix)
    ciphertext = ""

    for i in range(0, len(plaintext), n):
        block = plaintext[i:i + n]
        if len(block) < n:
            block += 'X' * (n - len(block))  # Tambahkan 'X' jika kurang panjang
        block_values = [ord(c) - ord('A') for c in block]
        
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += key_matrix[j][k] * block_values[k]
            ciphertext += chr((sum % 26) + ord('A'))

    return ciphertext

def hill_decrypt(ciphertext, key_matrix):
    n = len(key_matrix)
    determinant = int(round((key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]))) % 26
    inverse_determinant = mod_inverse(determinant, 26)

    # Hitung adjugate matrix
    adjugate_matrix = [
        [key_matrix[1][1], -key_matrix[0][1]],
        [-key_matrix[1][0], key_matrix[0][0]]
    ]

    # Inverse key matrix
    inverse_key_matrix = [[(inverse_determinant * adjugate_matrix[j][i]) % 26 for i in range(n)] for j in range(n)]

    plaintext = ""
    for i in range(0, len(ciphertext), n):
        block = ciphertext[i:i + n]
        block_values = [ord(c) - ord('A') for c in block]
        
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += inverse_key_matrix[j][k] * block_values[k]
            plaintext += chr((sum % 26) + ord('A'))

    return plaintext
