"""
    Given Assumptions:
     1) L, R are fields of 8-bits respectively
     2) Two rounds of encryption are applied to the given ciphertext
     3) Two keys are given which are both 1 byte in size
     4) f(R,k) = Reverse(R) XOR k

     NOTE: You will likely have to rewrite the frk if you use this script!

"""


def xor(a: str, b: str) -> str:
    sol = ""
    for i in range(0, 8):
        if a[i] != b[i]:
            sol += str(1)
        else:
            sol += str(0)
    return sol


# First round of decryption
def fr_decrypt() -> str:
    ct = input("Enter Ciphertext (2 bytes):\n")
    left = ct[8:16]
    right = ct[0:8]
    k = bin(int(input("Enter Key (Decimal):\n")))
    k = k[0] + k[2:9]
    frk = xor(right[::-1], k)
    output_left = right
    output_right = xor(left, frk)
    sol = output_left + output_right
    print("Output: {}\n".format(sol))
    return sol


# n >= 2 rounds of decryption
def sr_decrypt(ct: str, key: str) -> str:
    left = ct[0:8]
    right = ct[8:16]
    key = key[0] + key[2:9]
    frk = xor(right[::-1], key)
    output_left = right
    output_right = xor(left, frk)
    sol = output_left + output_right
    print("Output: {}\n".format(sol))
    return sol


def convert_to_ascii_val(ct: str) -> str:
    char_1 = ct[8:16]
    char_2 = ct[0:8]
    sol = chr(int(char_1, 2)) + chr(int(char_2, 2))
    return "Plaintext Solution: {}\n".format(sol)


iter1 = fr_decrypt()
k_i = bin(int(input("Enter Key (Decimal):\n")))
iter2 = sr_decrypt(iter1, k_i)
print(convert_to_ascii_val(iter2))
