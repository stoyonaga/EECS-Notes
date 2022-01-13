pt = input("Enter Plaintext Mapping (Initial): \n")
ct = input("Enter Ciphertext Mapping (Post): \n")
k = ord(ct) - ord(pt)

# Generate Map 1 Entries via Loop
charMapping = {}
numberMapping = {}
counter = 0

for char in range(97, 123):
    charMapping[chr(char)] = counter
    numberMapping[counter] = chr(char)
    counter += 1
# Begin Decryption of Ciphertext
inputReader = open("input.txt", "r")
newChar = None
for line in inputReader.readlines():
    for char in line:
        if char.lower() in charMapping.keys():
            print(numberMapping[(charMapping[char.lower()] - k) % 26], end="")
        else:
            print(char, end="")
print()
inputReader.close()

