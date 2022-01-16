def num_key(key: list) -> list:
    # A method that returns the key permutation as a list.
    ascii_rep = list()
    sol = list(key)
    counter = 0
    for entry in key:
        ascii_rep.append(ord(entry))
    for i in range(0, len(ascii_rep)):
        tmp_index = ascii_rep.index(min(ascii_rep))
        sol[tmp_index] = counter
        ascii_rep[tmp_index] = 9999
        counter += 1
    return sol


def generate_grid(inp: str, key_num: list) -> list:
    # Generate and return a grid representation of the plaintext
    inp = inp.replace(" ", "")

    # Variables
    sol_key = list()
    sol_key.append(key_num)
    k = len(inp) // len(key_num)
    for i in range(0, k):
        sol_key.append(list(key_num))
    chr_ptr = 0
    counter = 0

    for i in range(0, len(sol_key)):
        for j in range(0, len(sol_key[0])):
            if sol_key[0][j] == counter:
                depth = 1
                while depth < len(sol_key):
                    if chr_ptr < len(inp):
                        sol_key[depth][j] = inp[chr_ptr]
                        depth += 1
                        chr_ptr += 1
                    else:
                        sol_key[depth][j] = ";"
                        depth += 1
                        chr_ptr += 1
                counter += 1
    return sol_key


def decrypt(sol: list) -> str:
    ptxt = ""
    for i in range(1, len(grid)):
        for j in range(0, len(grid[i])):
            ptxt += sol[i][j]
    return ptxt


ciphertext = input("Enter ciphertext: \n")
ciphertext = ciphertext.replace(" ", "")

keyIn = list(input("Enter key: \n"))
index_key = num_key(keyIn)
grid = generate_grid(ciphertext, index_key)
print(decrypt(grid))
