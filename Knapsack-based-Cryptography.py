# Encrypt your first name into a binary string, each letter is encoded by 5 bits. 
# A is encoded to 00000
# B is encoded to 00001 
# ...

# Bui Van Thanh - 20200585
from math import gcd
import random

ID = 85 # two last digit in my student ID

def encode_string(string):
    bit_string = ''
    for i in string:
        bit_string += '{0:05b}'.format(ord(i.capitalize()) - ord('A'))
    return bit_string

def is_valid_string(string):
    string = string.upper() 
    for letter in string:
        if letter < 'A' or letter > 'Z':
            return False
    return True

def generate_super_increasing_vector(length): # super increasing vector 
    a = []
    total_sum = 2

    for _ in range(length + 1):
        random.seed(2) # make the same results when running in multiple times  
        element = random.randint(total_sum + 1, total_sum + 100)
        a.append(element)
        total_sum += element
    m = a[-1]
    w = ID + 1
    while True:
        if gcd(m, w) == 1:
            break
        else:
            w += 1
    return a[:-1], m, w

def generate_public_key(increasing_vector, m, w):
    return [(a_i * w) % m for a_i in increasing_vector] 

def encrypt(public_key, encoded_string):
    print("Encoded name: " + encoded_string)
    T = 0
    for i in range(len(public_key)):
        T += public_key[i] * int(encoded_string[i])
    return T

def decrypt(a, m, w, T):
    X = pow(w, -1, m)
    res = ''
    T_prime = (X * T) % m
    
    for element in reversed(a):
        if T_prime >= element:
            T_prime -= element
            res = '1' + res
        else:
            res = '0' + res
    return res

def decode_string(bit_sequence):
    decoded_string = ""
    for i in range(0, len(bit_sequence), 5):
        binary_code = bit_sequence[i:i+5]
        char_code = int(binary_code, 2) + ord('A')
        char = chr(char_code)
        decoded_string += char
    return decoded_string

def main():
    name = input("Enter your name: ")
    if not is_valid_string(name):
        print("Invalid name: ", name)
        return
    encoded_name = encode_string(name)
    a, m, w = generate_super_increasing_vector(len(encoded_name)) 
    public_key = generate_public_key(a, m, w)
    T = encrypt(public_key, encoded_name)
    T_prime = decrypt(a, m, w, T)
    original_string = decode_string(T_prime)

    print("Private key: ")
    print("a: ", a)
    print("m: ", m)
    print("w: ", w)

    print()
    print("Generating public key: ", public_key)
    print()

    print("Encrypted value: ", T)
    print("Decrypted value: ", T_prime)
    print("Original value: ", original_string)

if __name__ == '__main__':
    main()

