from hashlib import sha256

with open("Bip39-wordlist.txt", "r") as wordlist_file:
    words = [word.strip() for word in wordlist_file.readlines()]

def calculate_sizes(number_of_words):
    if   number_of_words==12: size_ENT=128
    elif number_of_words==15: size_ENT=160
    elif number_of_words==18: size_ENT=192
    elif number_of_words==21: size_ENT=224
    elif number_of_words==24: size_ENT=256
    else: exit()

    size_CS=int(size_ENT/32)
    return size_ENT,size_CS

def bits2bytes(bits):
    assert (len(bits)%8==0)    
    bytes_chunks = [bits[i:i+8] for i in range(0, len(bits), 8)]
    bytes_list = [int(chunk, 2) for chunk in bytes_chunks]
    return bytes(bytes_list)

def number2bits(n,length):
    resulting_string=format(n,'b')
    starting_zeros='0'*(length-len(resulting_string))
    return starting_zeros+resulting_string

def calculate_last_word(random_bit_string,extra_number=0,size_CS=1,extra_bits=3):
    local_random_bit_string=random_bit_string[:]
    extra_number_in_bits=number2bits(extra_number,extra_bits)

    local_random_bit_string+=extra_number_in_bits
    local_random_bytes_string=bits2bytes(local_random_bit_string)
    hash=sha256(local_random_bytes_string).digest()
    bhash=''.join(format(byte, '08b') for byte in hash)
    CS=bhash[:size_CS]
    final_entropy=local_random_bit_string+CS

    extracted_bits=final_entropy[-11:]
    word_index=int(extracted_bits,2)
    return word_index

mnemonic_string=input("Write the words separated by a space. And then click enter/return \n")
mnemonic=mnemonic_string.split()

indices = [words.index(word) for word in mnemonic]
number_of_words=len(indices)+1
size_ENT,size_CS=calculate_sizes(number_of_words)

random_bit_string=""
for i in indices:    
    random_bit_string+=number2bits(i,11)

size_ENT_so_far=len(random_bit_string)

missing_entropy_bits=size_ENT-size_ENT_so_far
number_possible_words=2**missing_entropy_bits

print("\nPossible last words:")
for t in range(number_possible_words):
    n=calculate_last_word(random_bit_string,t,size_CS,missing_entropy_bits)
    print(words[n])