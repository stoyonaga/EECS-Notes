# Lines 2 - 19 have been provided by Professor Zabrocki! 
def numb_to_vig_key(b):
    if b==0:
        return []
    else:
        return numb_to_vig_key(floor(b/26))+ [int(mod(b, 26))]
def numb_to_vig_key_nonrec(b):
    out = []
    while b>0:
        out = [int(mod(b,26))] + out
        b = floor(b/26)
    return out
def numb_to_vig_key_nonrec_2(b):
    k = floor(log(b)/log(26)) # number of digits of b mod 26
    return [int(mod(floor(b/26^(k-i)),26)) for i in range(k+1)]
def vig_key_from_integer(b):
    return "".join([chr(65+i) for i in numb_to_vig_key_nonrec_2(b)])
#


# Givens
prime = 98342967861236119818621441897795918589514011350299
primitive_root = 75991699467605793428239719497348878179115731651277
zabrocki_public_key = 77927873097883682289174534212022590683033519171186
my_secret_key = 68988219779411500
ciphertext = "KRNUGLPYSFIOLUKHDGQHQEXOCRSPMQV"

# Required Calculations

generator = primitive_root % prime 
my_public_key = power_mod(generator, my_secret_key, prime)
print("a) Public Key: {}".format(vig_key_from_integer(my_public_key)))

common_key = power_mod(zabrocki_public_key, my_secret_key, prime)
print("b) Common Key: {}".format(vig_key_from_integer(common_key)))
