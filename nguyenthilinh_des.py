# Constants for DES
INITIAL_PERMUTATION = [58, 50, 42, 34, 26, 18, 10, 2,
                       60, 52, 44, 36, 28, 20, 12, 4,
                       62, 54, 46, 38, 30, 22, 14, 6,
                       64, 56, 48, 40, 32, 24, 16, 8,
                       57, 49, 41, 33, 25, 17, 9, 1,
                       59, 51, 43, 35, 27, 19, 11, 3,
                       61, 53, 45, 37, 29, 21, 13, 5,
                       63, 55, 47, 39, 31, 23, 15, 7]

FINAL_PERMUTATION = [40, 8, 48, 16, 56, 24, 64, 32,
                     39, 7, 47, 15, 55, 23, 63, 31,
                     38, 6, 46, 14, 54, 22, 62, 30,
                     37, 5, 45, 13, 53, 21, 61, 29,
                     36, 4, 44, 12, 52, 20, 60, 28,
                     35, 3, 43, 11, 51, 19, 59, 27,
                     34, 2, 42, 10, 50, 18, 58, 26,
                     33, 1, 41, 9, 49, 17, 57, 25]

EXPANSION_PERMUTATION = [32, 1, 2, 3, 4, 5,
                         4, 5, 6, 7, 8, 9,
                         8, 9, 10, 11, 12, 13,
                         12, 13, 14, 15, 16, 17,
                         16, 17, 18, 19, 20, 21,
                         20, 21, 22, 23, 24, 25,
                         24, 25, 26, 27, 28, 29,
                         28, 29, 30, 31, 32, 1]

PERMUTED_CHOICE_1 = [57, 49, 41, 33, 25, 17, 9,
                     1, 58, 50, 42, 34, 26, 18,
                     10, 2, 59, 51, 43, 35, 27,
                     19, 11, 3, 60, 52, 44, 36,
                     63, 55, 47, 39, 31, 23, 15,
                     7, 62, 54, 46, 38, 30, 22,
                     14, 6, 61, 53, 45, 37, 29,
                     21, 13, 5, 28, 20, 12, 4]

ROUND_SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

PERMUTED_CHOICE_2 = [14, 17, 11, 24, 1, 5,
                     3, 28, 15, 6, 21, 10,
                     23, 19, 12, 4, 26, 8,
                     16, 7, 27, 20, 13, 2,
                     41, 52, 31, 37, 47, 55,
                     30, 40, 51, 45, 33, 48,
                     44, 49, 39, 56, 34, 53,
                     46, 42, 50, 36, 29, 32]

P_BOX = [16, 7, 20, 21, 29, 12, 28, 17,
         1, 15, 23, 26, 5, 18, 31, 10,
         2, 8, 24, 14, 32, 27, 3, 9,
         19, 13, 30, 6, 22, 11, 4, 25]

S_BOXES = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]
]


# split list into chunks of size n
def n_split(array, n):
    return [array[i: i + n] for i in range(0, len(array), n)]


# convert value to binary of bitSize
def bin_value(val, bitSize):
    binVal = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    # Appending with required number of zeros in front
    while len(binVal) < bitSize:
        binVal = "0" + binVal

    return binVal


# convert string to binary
def char_to_bits(text):

    # Initializing variable required
    bitString = ''
    for letter in text:
        # Getting binary (8-bit) value of letter
        binVal = bin_value(letter, 8)
        # Making list of the bits
        # Append the binary value to the bitString
        bitString += binVal
    return bitString


# convert array bit to char
def bit_array_to_string(array):
    # Chunking array of bits to 8 sized bytes
    byteChunks = n_split(array, 8)
    result = ''.join([chr(int(byte, 2)) for byte in byteChunks])
    # Returning result
    return result


# Perform permutation on data based on the provided permutation table
def permute(data, permutation):
    return ''.join(data[i - 1] for i in permutation)


# Perform a circular left shift on the data
def circular_left_shift(data, shift_amount):
    return data[shift_amount:] + data[:shift_amount]


# Perform XOR operation on two binary strings of the same length
def xor(data1, data2):
    return ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(data1, data2))


# Implement the sub-key generation algorithm
# generate 16 subkeys for DES algorithm
# input key: 54-bit binary string
# output: list of 16 subkeys, each represented as a 48-bit binary string
def generate_subkeys(key):
    # 1. perform an initial permutation on the 64-bit key into 56-bit key
    key = permute(key, PERMUTED_CHOICE_1)

    # split 56-bit key into two 28-bit halves
    left_half, right_half = key[:28], key[28:]

    # 2. leftshift and 3. contraction permutation
    subkeys = []
    for round_num in range(16):
        left_half = circular_left_shift(left_half, ROUND_SHIFTS[round_num])
        right_half = circular_left_shift(right_half, ROUND_SHIFTS[round_num])

        # combine the two halves and perform permuted choice 2
        combined_key = left_half + right_half
        subkey = permute(combined_key, PERMUTED_CHOICE_2)
        subkeys.append(subkey)

    return subkeys


# Implement the f-function
# Input data: 32-bit binary string, and subkey is a 48-bit binary string.
# Output: a 32-bit binary string.
def f_function(data, subkey):
    # 1. expand the 32-bit data to 48 bits
    expanded_data = permute(data, EXPANSION_PERMUTATION)

    # 2. XOR the expanded data with the subkey
    xor_result = xor(subkey, expanded_data)

    # 3. Apply the S-boxes
    # 3.1. split data into 6-bit blocks
    blocks = n_split(xor_result, 6)
    sbox_output = ""

    # 3.2 apply each s-box to its corresponding block
    for i, block in enumerate(blocks):
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        sbox_value = S_BOXES[i][row][col]
        # Convert the sbox value to binary string
        binVal = bin_value(sbox_value, 4)
        # Appending to result
        sbox_output += binVal

    # 4. Apply P-box
    f_output = permute(sbox_output, P_BOX)

    return f_output


def main():
    print()
    plaintext = input("Enter the message to be encrypted: ")
    key = input("Enter a key of 8 length (64-bits): ")
    print()

    # Checking if key is valid or not
    if len(key) != 8:
        print("Invalid Key. Key should be of 8 length (8 bytes).")
        return

    # add padding if plaintext is not divisible by 8
    paddingLength = 0
    if len(plaintext) % 8:
        paddingLength = 8 - len(plaintext) % 8
    plaintext += (chr(paddingLength) * paddingLength)

    # DES Encryption
    # generate subkeys
    key_in_bits = char_to_bits(key) # string of binary
    subkeys = generate_subkeys(key_in_bits)

    # format encode_plaintext to 64-bit block chunks
    plaintext8byteBlocks = n_split(plaintext, 8)
    result = ''

    for block in plaintext8byteBlocks:
        block = char_to_bits(block)

        # Do the initial permutation
        block = permute(block, INITIAL_PERMUTATION)

        # Splitting block into two 32-bit block
        left_half, right_half = block[:32], block[32:]
        temp = None

        # Do 16 round f-function
        for i in range(16):
            tmp = left_half
            left_half = right_half
            right_half = xor(tmp, f_function(right_half, subkeys[i]))

        # Swap again and Do final permutation
        result += permute(right_half + left_half, FINAL_PERMUTATION)

    print("Cipher text in binary format: " + result)
    # Convert bit array to string
    final_result = bit_array_to_string(result)

    print("Cipher text in string format: " + final_result)


if __name__ == '__main__':
    main()
