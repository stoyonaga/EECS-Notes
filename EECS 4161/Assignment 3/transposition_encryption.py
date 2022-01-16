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


def generate_grid(inp: str, key: list) -> list:
    # Generate and return a grid representation of the plaintext
    inp = inp.replace(" ", "")

    grid = list()
    grid_w = len(key)
    grid_h = len(inp) // grid_w + 1
    pt_pter = 0

    for i in range(0, grid_h):
        row = list()
        for j in range(0, grid_w):
            if pt_pter < len(inp):
                row.append(inp[pt_pter])
                pt_pter += 1
            else:
                row.append(";")
                pt_pter += 1
        grid.append(row)
    grid.insert(0, key)
    return grid


def encrypt(grid: list) -> str:
    sol = ""
    counter = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[0][j] == counter:
                depth = 1
                while depth < len(grid):
                    sol += str(grid[depth][j])
                    depth += 1
                counter += 1

    return sol


plaintext = input("Enter plaintext: \n")
char_key = input("Enter key (Character Rep): \n")
char_key = list(char_key)
print(generate_grid(plaintext, num_key(char_key)))
print(encrypt(generate_grid(plaintext, num_key(char_key))))
