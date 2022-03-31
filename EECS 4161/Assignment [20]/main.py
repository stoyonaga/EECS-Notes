"""
Assignment 20: RSA Breaking
Lines 5 - 9 have been supplied by Professor Zabrocki
"""
def numb_to_vig_key_nonrec(b):
    k = floor(log(int(b))/log(26)) # number of digits of b mod 26
    return [int(mod(floor(int(b)/26^(k-i)),26)) for i in range(k+1)]
def vig_key_from_integer(b):
    return "".join([chr(65+i) for i in numb_to_vig_key_nonrec(b)])

# Given Information
c = 
n = 
e = 

temp = str(factor(n)).split("*")
p = int(temp[0])
q = int(temp[1])

z = (p - 1) * (q - 1)
d = power_mod(e, -1, z)
m = power_mod(c, d, n)

plaintext = vig_key_from_integer(m)
print("a) The Plaintext is: " + plaintext)
print("b) The decrypting exponent is: " + str(d))
