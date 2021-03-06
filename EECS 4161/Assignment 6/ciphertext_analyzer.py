def generate_matrix(num_cols: int, num_rows: int) -> list:
    headers = []
    for i in range(1, num_cols + 1):
        headers.append(i)
    sol = []
    for i in range(0, num_rows):
        row = list()
        for j in range(0, num_cols):
            row.append(".")
        sol.append(row)
    sol.insert(0, headers)
    return sol


def print_matrix(matrix: list) -> None:
    for row in matrix:
        for entry in row:
            print("{}\t".format(entry), end="")
        print()


ciphertext = input("Enter Ciphertext: \n").replace(" ", "")

k2 = input("Enter the length of the second key: \n")
numCols = int(k2)
numRows = len(ciphertext)//int(k2)
print("The corresponding decryption table will have a column length of {0} and row length of {1}".format(k2, numRows))
print("Generating the empty matrix to load:")
rect = generate_matrix(numCols, numRows)
col_cntr = 0
char_ptr = 0
for r_idx in range(0, numCols):
    for c_idx in range(1, numRows + 1):
        rect[c_idx][r_idx] = ciphertext[char_ptr]
        char_ptr += 1
print_matrix(rect)
