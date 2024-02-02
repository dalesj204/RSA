import random
import math

# generates a prime efficiently
def generate_prime(bits):
    while True:
        # generate a random odd number of 'bits' length
        p = random.getrandbits(bits)
        p |= 2**(bits-1) | 1

        # check if the number is prime using the Miller-Rabin primality test
        if is_prime(p):
            return p
        
        
# checks if a number is prime efficiently
def is_prime(n):
    # check if n is divisible by 2
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # find r and d such that n = 2^r * d + 1
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # test for 'k' random bases using the Miller-Rabin test
    k = int(math.log(n, 2))  # k = log2(n)
    for i in range(k):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for j in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False

    return True


# to find if an inverse exists
def gcd(a, b):
    if a < b:
        a, b = b, a     # swap a and b so a is larger
    while b != 0:       # loop until b is 0, then we have found gcd
        a, b = b, a % b     # a is now b and b is now a % b
    return a   

# pulverizer/extended Euclidean algo
def pulverizer(a, b):
    # basis
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = pulverizer(b % a, a)
    
    # update x and y after recursive calls
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y

# turns characters in a string into their ascii values with new lines after each number
def to_ascii_str(text):
    ascii_txt = ''
    for character in text:
        ascii_txt+= str(ord(character)) + '\n'
        
    return ascii_txt

def CRT(y, d, p, q):
    a = pow(y, d % (p-1), p)
    b = pow(y, d % (q-1), q)
    return a, b


bit_length = int(input("Enter the bit length for the primes: "))
plain_name = raw_input("Enter the plain text file name (with .txt): ")
plain_file = open(plain_name, "r")
cipher_name = raw_input("Enter the cipher text file name (with .txt): ")
cipher_file = open(cipher_name, "w+")
ascii_msg = to_ascii_str(plain_file.read())
decrypted_name = raw_input("Enter the decrypted text file name (with .txt): ")
decrypted_file = open(decrypted_name, "w")


# GENERATE NUMBERS
p = generate_prime(bit_length)
q = generate_prime(bit_length)
n = p * q
phi = (p-1)*(q-1)
e = 2;   
    
    
while gcd(phi, e) != 1: # find e
    e+=1


z, x, inverse_e = pulverizer(phi, e)
d = inverse_e % phi

# print("e: " + str(e))
# print("n: " + str(n))



# ENCRYPTION
for line in ascii_msg.splitlines(): # strip the new lines
    num = int(line) # convert number to int
    y = pow(num, e, n) # ecryption algo: y = m^e mod n
    cipher_file.write(str(y) + "\n") # write the new number (str) into file with new line
    
    
# DECRYPTION

# find inverses for the primes
_, p_inverse, q_inverse = pulverizer(p, q)

# apply crt and decrypt the numbers in the message
cipher_file.seek(0) 
for line in cipher_file.read().splitlines():
    num = int(line)
    a, b = CRT(num, d, p, q)
    decrypted_file.write(chr((a*q*q_inverse + b*p*p_inverse) % n))

