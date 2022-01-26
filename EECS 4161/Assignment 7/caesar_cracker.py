"""
    NOTE: While brute-forcing the key is not ideal, the quantity of ciphertext will not
          allow for frequency analysis. Thus, this program was written for Assignment #7
"""
print("========== Caesar Cipher: Brute Force Cracker Program ==========")
k = 1
ct = input("Enter Ciphertext (Key Representation): \n")
# Generate Map 1 Entries via Loop
alphabet = list()
for char in range(0, 26):
    alphabet.append(chr(65 + char))
# Begin Decryption of Ciphertext
print(alphabet)
for j in range(1, 26):
    print("Key[{}] will produce the following plaintext:\t\t ".format(k), end="")
    for i in range(0, len(ct)):
        print(alphabet[alphabet.index(ct[i].upper()) - k % 26], end="")
    k = k + 1
    print()
