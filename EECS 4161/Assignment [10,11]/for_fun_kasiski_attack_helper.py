from matplotlib import pyplot as plt

'''
Critical Information:
    1) Make sure that you have the matplotlib library installed
    2) [Optional] Use vigenere_decryption.py from https://github.com/stoyonaga/EECS-Notes/tree/main/EECS%204161/Assignment%202 to test your solution(s)!
    3) [Refactor] caesar_graph_generator_p1.py has been re-used in this helper script
    4) [Internal Prerequisites] Professor Readings & Lecture Video(s)
    5) [External Prerequisites] Jeff Suzuki Videos on Incidence of Coincidence & Vigenere Cracking
       (Index of Coincidence: https://www.youtube.com/watch?v=raNO806R4yc)
       (Vigenere Cracking: https://www.youtube.com/watch?v=TxClRjnRNJw)
'''


# Format the ciphertext into a one-line representation (trimming newlines and any spaces for n-grams
def format_ciphertext():
    cipher_text = ""
    file = open("sample.txt", "r")
    for line in file.readlines():
        cipher_text += line.replace("\n", "")
    file.close()
    return cipher_text.replace(" ", "")


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
    return ic


# Calculate the period approximation of the given ciphertext
def period_approximation(cipher_text: str) -> int:
    num = 0.027 * len(cipher_text)
    n = len(cipher_text)
    den = (n * get_ic(cipher_text)) + 1 - (0.038 * n)
    return round(num / den)


# Generate a histogram to crack the Key using a Kasiski Attack
def generate_histogram(cipher_text: str, period) -> None:
    char_freq = {}
    index = int(input("Enter Index to Start the Frequency Analysis On: \n"))
    for i in range(65, 91):
        char_freq[chr(i)] = 0

    # Iterate through input and record number of characters read so far...
    while index < len(cipher_text):
        char_freq[ct[index].upper()] += 1
        index += period
    # Graphing the Character Frequency
    plt.style.use("seaborn")
    plt.bar(char_freq.keys(), char_freq.values(), label="Ciphertext")
    plt.xlabel("Characters")
    plt.ylabel("Frequency")
    plt.title("Ciphertext Character Frequency Visualizer")
    plt.legend()
    plt.show()


ct = format_ciphertext()
print("===== Generated Calculations =====")
print("IC: {}".format(get_ic(ct)))
print("Period: {}".format(period_approximation(ct)))
generate_histogram(ct, period_approximation(ct))
"""
(Starting our frequency analysis on 0, 4, 8, 12, ..., we can essentially guess the vigenere shift: E -> J) 
    F
(Starting our frequency analysis on 1, 5, 9, 13, ..., we can essentially guess the vigenere shift: E -> E)
    A
(Starting our frequency analysis on 2, 6, 10, 14, ..., we can essentially guess the vigenere shift: E -> G)
    C
(Starting our frequency analysis on 3, 7, 11, 15, ..., we can essentially guess the vigenere shift: E -> X)
    T
"""
