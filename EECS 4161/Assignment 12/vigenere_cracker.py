"""
This code is used to for lack of a better word, brute-force the key for a given
vigenere ciphertext.

We cannot apply the Kasiski attack, because the quantity of ciphertext is very small.
Thus, the most optimal way to crack this is to brute-force the key.

Lines 10 - 48 were written in class by Professor Zabrocki.
Lines 50 - 80 were implemented as an auxiliary function to brute-force the key.
"""
eng = [73, 9, 30, 44, 130, 28, 16, 35, 74, 2, 3, 35, 25, 78, 74, 27, 3, 77, 63, 93, 27, 13, 16, 5, 19, 1]
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def clean(txt):
    return "".join([a.upper() for a in txt if a.isalpha()])


def encrypt_vig(p_txt, ky):
    c_txt = clean(p_txt)
    return "".join([alpha[(alpha.index(c_txt[i]) + alpha.index(ky[i % len(ky)])) % 26] for i in range(len(c_txt))])


def decrypt_vig(p_txt, ky):
    c_txt = clean(p_txt)
    return "".join([alpha[(alpha.index(c_txt[i]) - alpha.index(ky[i % len(ky)])) % 26] for i in range(len(c_txt))])


def score_text(txt):
    counts = [txt.count(a) for a in alpha]
    return sum(counts[i] * eng[i] for i in range(26))


def best_caesar_shift(ct):
    scores = [score_text(decrypt_vig(ct, a)) for a in alpha]
    return alpha[scores.index(max(scores))]


def best_vig_keyword_fixed_length(ct, length):
    return "".join([best_caesar_shift("".join([ct[i] for i in range(len(ct)) if i % length == p]))
                    for p in range(length)])


ct_in = "REDACTED, PUT YOUR CIPHERTEXT HERE!!"


########################################################################################################################


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
    return ic


# Calculate the period approximation of the given ciphertext
def period_approximation(cipher_text: str) -> float:
    num = 0.027 * len(cipher_text)
    n = len(cipher_text)
    den = (n * get_ic(cipher_text)) + 1 - (0.038 * n)
    return round((num / den), 3)


print("Period Approximation (Based on Sample CT): {}".format(period_approximation(ct_in)))
for k in range(round(period_approximation(ct_in)), 10):
    print("Key assumption of length {} will produce the key guess of {}, thus producing the plaintext {}"
          .format(k, best_vig_keyword_fixed_length(ct_in, k), decrypt_vig(ct_in, best_vig_keyword_fixed_length(ct_in,
                                                                                                               k))))
