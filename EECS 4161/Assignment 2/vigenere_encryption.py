# Initial Variables
pt = input("Enter Plaintext: \n")
pt = list(pt)
key = input("Enter Key: \n")
key = list(key)

# Generate Dictionaries
charMapping = {}
numberMapping = {}
counter = 0
for char in range(97, 123):
    charMapping[chr(char)] = counter
    numberMapping[counter] = chr(char)
    counter += 1

char2 = 0
ct = None
for char1 in pt:
    if char1 in " ":
        print(" ", end="")
    elif char2 < len(key):
        print(numberMapping[(charMapping[char1.lower()] + charMapping[key[char2].lower()]) % 26] + "", end="")
        char2 += 1
    else:
        char2 = 0
        print(numberMapping[(charMapping[char1.lower()] + charMapping[key[char2].lower()]) % 26] + "", end="")
        char2 += 1
print()

