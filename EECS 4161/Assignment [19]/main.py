"""
Assignment 19: Elliptic curve ElGamal Submission
Lines 6 - 63 are provided by Professor Zabrocki

Lines 67 - 89 will need to be modified with your specific question inputs, where:
Y = (Y_x, Y_y) is Professor Zabrocki's ephemeral key * A
"""

# Elliptic curve addition mod p
# an elliptic curve is a triple ec = (a,b,p)
# (ideally) with 4a^3 - 27b^2 not equivalent to 0 mod p
# a point is a pair P = (x,y) with 0 <= x,y <= p
# such that y^2 = x^3 + a*x + b (mod p)
def add_pt(P, Q, ec):
    # add a point P and a point Q on an elliptic curve with parameters (a,b,p)
    # example: add_pt((2,6), (0,9), (2,5,19)) and the result is (5, 8)
    if P[0]==infinity:
        return (Q[0],Q[1])
    elif Q[0]==infinity:
        return (P[0],P[1])
    elif P[0]!=Q[0]:
        la = ((P[1]-Q[1])/(P[0]-Q[0]))%ec[2]
        rx = (la^2 - P[0] - Q[0])%ec[2]
        ry = (la*(rx-P[0])+P[1])%ec[2]
    elif P==Q and P[1]!=0:
        la = ((3*P[0]**2+ec[0])/(2*P[1]))%ec[2]
        rx = (la^2 - 2*P[0])%ec[2]
        ry = (la*(rx-P[0])+P[1])%ec[2]
    else:
        return (infinity, infinity)
    return (rx, (-ry)%ec[2])
def mult(a,P,ec):
    # multiply a point P by an integer a using Montgomery's ladder
    # example: mult(3, (2,6), (2,5,19)) and the result is (5, 8)
    if P[0]==infinity:
        return P
    if a<0:
        return mult(-a, (P[0],-P[1]), ec)
    if a==0:
        return (infinity, infinity)
    bina = bin(a)[2:] # the binary expansion of a
    x1 = P
    x2 = add_pt(P,P,ec)
    for i in range(1,len(bina)):
        if bina[i]=='0':
            x2 = add_pt(x1,x2,ec)
            x1 = add_pt(x1,x1,ec)
        else:
            x1 = add_pt(x1,x2,ec)
            x2 = add_pt(x2,x2,ec)
    return x1

# Code to compute the base-26 expansion of a number 
def numb_to_vig_key_nonrec(b):
    k = floor(log(int(b))/log(26)) # number of digits of b mod 26
    return [int(mod(floor(int(b)/26^(k-i)),26)) for i in range(k+1)]
def vig_key_from_integer(b):
    return "".join([chr(65+i) for i in numb_to_vig_key_nonrec(b)])
eng = [73,9,30,44,130,28,16,35,74,2,3,35,25,78,74,27,3,77,63,93,27,13,16,5,19,1]
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def clean(txt):
    return "".join([a.upper() for a in txt if a.isalpha()])
def decrypt_vig(ptxt, ky):
    cptxt = clean(ptxt)
    return "".join([alpha[(alpha.index(cptxt[i]) - alpha.index(ky[i%len(ky)]))%26] for i in range(len(cptxt))])
# -------------------------------------------------------------------------------

a = 
b = 
p = 
Ax = 
Ay = 
A = (Ax, Ay)
N = 

my_secret_key =  
my_public_key = mult(my_secret_key, A, (a, b, p))
print("a) My secret key is: {}".format(my_public_key))

# To communicate I send you the pair (Y, Z) with Y = (Y_x, Y_y) = an ephemeral secret key that I have chosen times the point A
Y_x = 
Y_y = 
Y = (Y_x, Y_y)


common_key = mult(my_secret_key, Y, (a, b, p))
print("b) The common key is: {}".format(common_key))
vig_key = vig_key_from_integer(common_key[1])

print("c) The plaintext is: {}".format(decrypt_vig("Z Inputs", vig_key)))


