"""
Assignment 18: ElGamal Public Key System Solution
Credit to Professor Zabrocki for the main implementation of this program.
"""
def numb_to_vig_key_nonrec(b):
    k = floor(log(int(b))/log(26)) # number of digits of b mod 26
    return [int(mod(floor(int(b)/26^(k-i)),26)) for i in range(k+1)]
def vig_key_from_integer(b):
    return "".join([chr(65+i) for i in numb_to_vig_key_nonrec(b)])

p = 
a = 
my_secret = 

# My Public Key
beta = power_mod(a, my_secret, p)

print("a) My Public Key: " + str(beta))

Y = []
Z = []

print("b) Resulting Plaintext Message")
for i in range(0, 3):
    print(vig_key_from_integer(mod(Z[i] * power_mod(Y[i], -my_secret, p), p)))

