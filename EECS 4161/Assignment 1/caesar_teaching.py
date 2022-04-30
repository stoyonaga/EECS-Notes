import time
from matplotlib import pyplot as plt
from collections import Counter
from collections import deque

""" |                                                                                   |                   
    |                               Caesar Cipher Tool Kit                              |
    |           (Encryption, Decryption, Graph Generation, Read from File(s))           |
"""


# Auxiliary Method
def generate_character_mapping() -> deque:
    alphabet = deque()
    for i in range(0, 26):
        alphabet.append(chr(65 + i))
    return alphabet


# Auxiliary Method
def generate_shift_mapping(alphabet: deque, key: int = 3) -> deque:
    result = deque(alphabet)
    result.rotate(-key)
    return result


# Auxiliary Method
def clean_text(fetch: str) -> str:
    char_set = ""
    sol = ""
    for i in range(0, 26):
        char_set += chr(65 + i)
    for character in fetch:
        if character.upper() in char_set:
            sol += character.upper()
        else:
            pass
    return sol


# Auxiliary Method
def read_file(fn: str) -> str:
    sol = ""
    line_grabber = open(fn, "r")
    for line in line_grabber.readlines():
        sol += line
    line_grabber.close()
    return sol


# Useful for demonstrating how Caesar Cipher Works
def generate_mapped_pairing() -> int:
    pt = input("Enter Plaintext Mapping (Initial): ")
    encrypted_pt = input("Enter Ciphertext Mapping to the Initial Plaintext (Post): ")
    print("==========")
    temp_key = ord(encrypted_pt) - ord(pt)
    key = temp_key if temp_key > 0 else -temp_key
    print("Key: {}".format(key))
    char_set = generate_character_mapping()
    key_set = generate_shift_mapping(char_set, ord(encrypted_pt) - ord(pt))
    print(char_set)
    print(key_set)
    return key


# Encrypting Algorithm
def encrypt_caesar(key: int = 3) -> str:
    encryption = ""
    pt = input("Enter Plaintext: ")
    # Generate Necessary Map Entries via Loop
    char_mapping = {}
    number_mapping = {}
    counter = 0
    for char in range(65, 91):
        char_mapping[chr(char)] = counter
        number_mapping[counter] = chr(char)
        counter += 1

    for character in pt:
        # Only Encrypt Characters
        if character.upper() in char_mapping.keys():
            encryption += str(number_mapping[(char_mapping[character.upper()] + key) % 26])
        # Maintain Special Grammatical Character(s)
        else:
            encryption += str(character)
    return str(encryption)


def encrypt_caesar_file(pt: str, key: int = 3) -> str:
    encryption = ""
    # Generate Necessary Map Entries via Loop
    char_mapping = {}
    number_mapping = {}
    counter = 0
    for char in range(65, 91):
        char_mapping[chr(char)] = counter
        number_mapping[counter] = chr(char)
        counter += 1

    for character in pt:
        # Only Encrypt Characters
        if character.upper() in char_mapping.keys():
            encryption += str(number_mapping[(char_mapping[character.upper()] + key) % 26])
        # Maintain Special Grammatical Character(s)
        else:
            encryption += str(character)
    return str(encryption)


# Decrypting
def decrypt_caesar(encrypted_pt: str, key: int) -> str:
    decryption = ""

    char_mapping = {}
    number_mapping = {}
    counter = 0
    for char in range(65, 91):
        char_mapping[chr(char)] = counter
        number_mapping[counter] = chr(char)
        counter += 1

    for character in encrypted_pt:
        # Only Decrypt Characters
        if character.upper() in char_mapping.keys():
            decryption += str(number_mapping[(char_mapping[character.upper()] - key) % 26])
        # Maintain Special Grammatical Character(s)
        else:
            decryption += str(character)
    return str(decryption)


# This method will only work well on large samples of text
def generate_possible_key_candidates(encrypted_pt: str):
    possible_keys = Counter(clean_text(encrypted_pt)).most_common(10)
    print("===== 10 Most Frequently Appearing Characters (Frequency Analysis =====")
    print(possible_keys)
    for key in possible_keys:
        temp_key = ord(key[0]) - ord("A")
        key = temp_key if temp_key > 0 else -temp_key
        print("Key {} will produce a plaintext of {}".format(key, decrypt_caesar(encrypted_pt, key)))
        time.sleep(2)


"""
Display only the frequency of the characters that appear in the ciphertext to quickly estimate which 
keys are possible candidate solution(s)
"""


def generate_frequency_analysis_graph(encrypted_pt: str) -> None:
    characters = Counter(clean_text(encrypted_pt))
    sorted(characters.keys())
    plt.style.use("seaborn")
    plt.title("Compressed Frequency Analysis")
    plt.xlabel("Characters")
    plt.ylabel("Frequency")
    plt.bar(characters.keys(), characters.values())
    plt.show()


print("========== Caesar Cipher Tool-Kit Version 1.0.0 ==========")

# Demonstration 1: Encryption, Decryption, Frequency Analysis
# Note: This reads the plaintext from the terminal. Use the other demo with a .txt file for large plaintext / ciphertext
print("Teaching Illustration: ")
ct = encrypt_caesar(generate_mapped_pairing())
generate_possible_key_candidates(ct)
print("===== Generating the Compressed Frequency Analysis Graph")
generate_frequency_analysis_graph(ct)

"""
# Demonstration 2: Encryption, Decryption, Frequency Analysis
plaintext = read_file("input.txt")
ct = encrypt_caesar_file(plaintext, 110)
generate_frequency_analysis_graph(ct)
generate_possible_key_candidates(ct)
"""
