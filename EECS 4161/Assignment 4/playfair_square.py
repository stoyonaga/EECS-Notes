def generate_pf_square(key: str) -> list:
    key_list = list()
    psq = list()
    table_entries = {"J": "x"}
    ascii_ptr = 65
    c_ptr = 0
    j = 0

    # Insert Key into the top-row of the playfair square (Removing the repetitions of letters, of course.)
    for i in range(len(key)):
        if key[i].upper() not in key_list and key[i].upper() not in table_entries.keys():
            table_entries[key[i].upper()] = "x"
            key_list.append(key[i].upper())
    for i in range(0, 5):
        entry = list()
        while j in range(0, 5):
            if c_ptr < len(key_list):
                entry.append(key_list[c_ptr])
                c_ptr += 1
                j += 1
            else:
                if chr(ascii_ptr) not in table_entries.keys():
                    table_entries[chr(ascii_ptr)] = "x"
                    entry.append(chr(ascii_ptr))
                    ascii_ptr += 1
                    j += 1
                else:
                    ascii_ptr += 1
        j = 0
        psq.append(entry)
    return psq


k = input("Please enter the key: \n")
ps = generate_pf_square(k)
for item in ps:
    print(item)
