# ========== Part 1: Assignment # 10 ==========

# Format the ciphertext into a one-line representation (trimming newlines and any spaces for n-grams
def format_ciphertext():
    cipher_text = ""
    file = open("input.txt", "r")
    for line in file.readlines():
        cipher_text += line.replace("\n", "")
    file.close()
    return cipher_text.replace(" ", "")


def get_adj_pairs(ct: str) -> int:
    counter = 0
    for i in range(0, len(ct) - 1):
        if ct[i] == ct[i + 1]:
            counter += 1
    return counter


def ratio_test(ct: str) -> float:
    numerator = get_adj_pairs(ct)
    denominator = len(ct) - 1
    return round(numerator/denominator, 3)

# ========== Part 2: Assignment # 11 ==========


# Calculate the Index of Coincidence via Ciphertext
def get_ic(cipher_text: str) -> float:
    ic = 0
    num = 0
    alphabet = {}
    den = len(cipher_text)
    den *= den - 1

    for i in range(65, 91):
        alphabet[chr(i)] = 0
    for j in range(0, len(cipher_text)):
        alphabet[cipher_text[j].upper()] += 1
    for key in alphabet.keys():
        num += alphabet[key] * (alphabet[key] - 1)
    ic += num / den
    return round(ic, 3)


# Calculate the period approximation of the given ciphertext
def period_approximation(cipher_text: str) -> float:
    num = 0.027 * len(cipher_text)
    n = len(cipher_text)
    den = (n * get_ic(cipher_text)) + 1 - (0.038 * n)
    return round((num / den), 2)


print("========== Assignment #10 Solutions ==========")
c_entry = format_ciphertext()
print("1) The number of equal adjacent letters is: " + str(get_adj_pairs(c_entry)))
print("2) The number of characters in the ciphertext is: " + str(len(c_entry)))
print("3) Ratio Value: {}".format(ratio_test(c_entry)))
print("4) Yes, the conclusion drawn from part 3) agrees with the period I was given. "
      "That is, this ciphertext was "
      "encoded using a Vigenere Cipher.")
print("========== Assignment #11 Solutions ==========")
print("1) The value of the IC is: " + str(get_ic(c_entry)))
print("2) The approximation for the Vigenere period is: " + str(period_approximation(c_entry)))
print("3) The accuracy of the formula for a period is not very good in this specific case. "
      "This is due to the fundamental fact that there is not a sufficient amount of ciphertext to analyze.")
