"""
================================================================
Assignment #13: Break Rectangular Transposition (Encrypted File)
================================================================

This is a helper script that will brute-force the key for a rectangular transposition cipher.
    -   63 - 82 and 123 - 129 have been written into Professor Zabrocki's Code
    -   The given code has been translated to work without Sage (Pure Python)

Do note that you will have to know the length of the key in addition to its first and last value(s).
"""

import math
import itertools


def clean(txt):
    return "".join([a.upper() for a in txt if a.isalpha()])


def encrypt_rt(pt, perm):
    cpt = clean(pt)
    cpt += cpt[:int((-len(cpt)) % len(perm))]  # make sure its a multiple of len(perm)
    return "".join(
        [cpt[perm.index(j + 1) + i * len(perm)] for j in range(len(perm)) for i in
         range(math.floor(len(cpt) / len(perm)))])


def decrypt_rt(ct, perm):
    cct = clean(ct)
    if len(cct) % len(perm):
        raise ValueError("The length of the permutation=%s must divide the length of the cyphertext=%s!" % (
            len(perm), len(ct)))
    return "".join([cct[math.floor((perm[j] - 1) * len(cct) / len(perm) + i)] \
                    for i in range(math.floor(len(cct) / len(perm))) for j in range(len(perm))])


def rt_counts(seg1, seg2):
    if len(seg1) != len(seg2):
        raise ValueError("Segments don't have the same length")
    counts = [[0] * 26 for a in range(26)]
    for ii in range(len(seg1)):
        counts[alpha.index(seg1[ii])][alpha.index(seg2[ii])] += 1
    return counts


def rt_stat(seg1, seg2):
    if seg1 == seg2:
        return 0
    counts = rt_counts(seg1, seg2)
    return math.floor(100 * sum(float(biletter[ss][tt]) * math.log(float(counts[ss][tt])) / blettotal \
                                for ss in range(26) for tt in range(26) if counts[ss][tt]))


def rt_stat_matrix(ct, period):
    cct = clean(ct)
    cct += cct[:int((-len(cct)) % period)]  # make sure its a multiple of len(perm)
    N = len(cct)
    segs = [cct[i * N // period:(i + 1) * N // period] for i in range(period)]
    return [[rt_stat(segs[j], segs[i]) for j in range(period)] for i in range(period)]


def rt_stat_matrix_bf() -> None:
    for i in range(4, 10):
        for entry in rt_stat_matrix(ct_in, i):
            print(entry)
        print("Key: {}\n".format(i))


def brute_force(permutation: list, fk: int, lk: int) -> None:
    subset_bf = list(itertools.permutations(permutation))
    attempt = []
    for i in range(0, len(subset_bf)):
        attempt.clear()
        for j in range(0, len(subset_bf[0])):
            attempt.append(subset_bf[i][j])
        attempt.insert(0, fk)
        attempt.append(lk)
        print("==========")
        print("Key: {}".format(attempt))
        print(decrypt_rt(ct_in, attempt))
        print("==========\n")


alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # the English alphabet
biletter = [
    [9, 796, 1028, 893, 564, 717, 922, 1514, 325, 1077, 338, 1148, 1559, 470, 72, 1163, 0, 878, 517, 529, 294, 641,
     1961, 575, 501, 1949],
    [26, 7, 0, 2, 5, 0, 0, 0, 11, 0, 3, 2, 46, 0, 14, 0, 0, 4, 1, 0, 57, 0, 1, 0, 4, 0],
    [108, 4, 54, 7, 120, 0, 0, 3, 213, 0, 0, 6, 7, 173, 45, 1, 0, 47, 79, 10, 136, 0, 0, 312, 28, 0],
    [177, 3, 1, 82, 451, 0, 6, 3, 173, 0, 10, 278, 0, 635, 87, 0, 0, 106, 10, 0, 91, 8, 12, 0, 26, 0],
    [26, 4197, 2225, 4926, 571, 1673, 3121, 7332, 569, 2370, 6887, 2501, 3879, 1580, 48, 2278, 0, 3644, 2340, 1847, 565,
     7842, 2532, 1654, 3777, 5942],
    [28, 0, 0, 2, 41, 267, 0, 0, 37, 0, 8, 30, 2, 29, 375, 0, 0, 8, 6, 2, 15, 0, 0, 0, 0, 0],
    [46, 0, 0, 26, 24, 0, 35, 0, 55, 0, 0, 21, 0, 276, 16, 0, 0, 34, 0, 0, 76, 0, 0, 0, 0, 0],
    [10, 0, 674, 3, 11, 0, 676, 2, 1, 0, 104, 0, 0, 6, 13, 125, 0, 8, 296, 1854, 5, 0, 750, 39, 0, 0],
    [300, 379, 477, 1130, 99, 1008, 526, 731, 10, 219, 991, 953, 843, 416, 57, 265, 0, 740, 737, 881, 161, 1610, 1319,
     701, 432, 1349],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 13, 0, 1, 0, 0, 0, 2, 0, 4, 3, 0, 2, 3, 0, 0, 8, 3, 0, 0, 0, 0, 0, 1, 0],
    [356, 421, 125, 42, 154, 101, 68, 5, 192, 0, 67, 479, 3, 24, 141, 275, 0, 55, 49, 34, 371, 0, 13, 0, 58, 43],
    [69, 12, 3, 44, 84, 2, 6, 3, 73, 0, 6, 20, 162, 25, 175, 18, 0, 75, 27, 10, 81, 2, 0, 18, 94, 0],
    [1327, 0, 7, 37, 976, 6, 318, 26, 1766, 0, 399, 2, 29, 137, 1548, 4, 0, 229, 14, 10, 1072, 0, 252, 0, 121, 0],
    [6, 768, 1819, 584, 31, 2222, 908, 626, 711, 2508, 157, 620, 993, 420, 176, 1204, 0, 887, 562, 979, 15, 422, 1029,
     59, 1758, 403],
    [44, 0, 0, 0, 38, 0, 0, 0, 19, 0, 0, 8, 143, 0, 58, 115, 0, 10, 76, 0, 76, 0, 0, 697, 61, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [798, 448, 288, 219, 1304, 822, 897, 103, 231, 47, 57, 23, 17, 7, 1035, 1561, 0, 143, 18, 324, 988, 0, 71, 0, 209,
     0],
    [607, 139, 52, 300, 747, 15, 155, 16, 724, 0, 668, 236, 148, 455, 216, 109, 0, 397, 507, 253, 741, 13, 222, 0, 920,
     0],
    [1644, 51, 933, 13, 422, 518, 258, 243, 1186, 0, 29, 265, 5, 1714, 413, 299, 0, 622, 2594, 222, 1311, 0, 16, 1793,
     179, 0],
    [34, 181, 86, 149, 11, 115, 127, 21, 2, 835, 6, 66, 83, 30, 235, 113, 2490, 47, 144, 48, 7, 2, 0, 0, 34, 31],
    [19, 1, 0, 9, 19, 0, 0, 0, 23, 0, 0, 5, 0, 6, 30, 0, 0, 13, 0, 0, 1, 1, 0, 0, 0, 0],
    [8, 0, 0, 5, 30, 0, 0, 1, 0, 0, 0, 1, 0, 2, 51, 0, 0, 2, 5, 13, 0, 0, 0, 0, 15, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0],
    [62, 231, 18, 52, 24, 8, 10, 8, 0, 0, 22, 162, 38, 31, 8, 3, 0, 60, 16, 40, 2, 11, 4, 0, 13, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]]
bletsums = [sum(row) for row in biletter]
blettotal = sum(bletsums)

file_open = open("input.txt", "r")
ct_in = ""
for line in file_open.readlines():
    ct_in += clean(line)
file_open.close()

brute_force([1, 3, 5], 4, 2)
