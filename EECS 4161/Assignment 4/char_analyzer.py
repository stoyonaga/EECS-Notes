# A simple program to determine which characters are required to generate the remaining key!!
ciphertext = input("Enter ciphertext: ")
alphabet = {"*": 0}
ascii_pntr = 65

for i in range(1, 27):
    if ascii_pntr != 74:
        alphabet[chr(ascii_pntr)] = 0
    ascii_pntr += 1
for i in range(0, len(ciphertext)):
    alphabet[ciphertext[i].upper()] += 1

print("===== Tabulated Results =====")
for key in alphabet.keys():
    print("{} -> {}".format(key, alphabet[key]))
