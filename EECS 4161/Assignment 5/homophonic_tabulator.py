def generate_initial_rect(k: list):
    ascii_ptr = 65
    sol = list()
    alph = list()
    y_index = 0
    val = 25
    for i in range(0, 26):
        alph.append(chr(ascii_ptr))
        ascii_ptr += 1
    alph.remove("J")
    sol.append(alph)
    for i in range(0, len(k)):
        row = list()
        for j in range(0, 25):
            row.append("")
        sol.append(row)
    return sol


def generate_key_indices(k: list):
    ascii_ptr = 65
    inputs = list()
    indices = list()
    for i in range(0, 26):
        inputs.append(chr(ascii_ptr))
        ascii_ptr += 1
    inputs.remove("J")

    for char in k:
        indices.append(inputs.index(char) - 1)
    return indices


def fill_rectangle(rect: list, key_indices: list) -> list:
    sol = rect
    val = 25
    key_ptr = 0
    for y in range(1, len(rect)):
        for x in range(0, 25):
            sol[y][key_indices[key_ptr] - x] = val
            val -= 1
        val = 25
        key_ptr += 1

    const = 25
    if len(rect) >= 2:
        for y in range(2, len(rect)):
            for x in range(0, len(rect[0])):
                sol[y][x] += const
            const += 25
    return sol


def rectangle_tostring(sol: list) -> None:
    for row in sol:
        for char in row:
            print("{}\t".format(char), end="")
        print()


key = list(input("Enter a key (Character(s)): \n").upper().replace(" ", ""))
initial_rect = generate_initial_rect(key)
num_key = generate_key_indices(key)
total_rect = fill_rectangle(initial_rect, num_key)
rectangle_tostring(initial_rect)
