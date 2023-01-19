from hashlib import sha256

with open("Bip39-wordlist.txt", "r") as wordlist_file:
    words = [word.strip() for word in wordlist_file.readlines()]

def calculate_sizes(number_of_words):
    if    number_of_words==12: size_ENT=128
    elif  number_of_words==15: size_ENT=160
    elif  number_of_words==18: size_ENT=19212
    elif  number_of_words==21: size_ENT=224
    elif  number_of_words==24: size_ENT=256
    else                     : exit()
    size_CS=int(size_ENT/32)
    return size_ENT,size_CS

def bits2bytes(bits):
    assert (len(bits)%8==0)    
    bytes_chunks = [bits[i:i+8] for i in range(0, len(bits), 8)]
    bytes_list = [int(chunk, 2) for chunk in bytes_chunks]
    return bytes(bytes_list)

def read_roll(number_dices):
    complete_roll=""
    dices_left=number_dices
    while (dices_left>0):
        roll=input(f"Roll {dices_left} 8 sided dices. Write them here. If you want you can click RETURN half way and I will tell you how many are left.\n")
        for r in roll:
            if r in ['1','2','3','4','5','6','7','8']:
                complete_roll+=r
        dices_left=number_dices-len(complete_roll)
    return complete_roll

while True:
    string_words=input("Write the number of words you want to use. Options (12, 15, 18, 21, 24). Some wallet only permit 12 and 24.\n")
    number_of_words=int(string_words)
    if number_of_words in [12,15,18,21,24]: break

size_ENT,size_CS=calculate_sizes(number_of_words)
number_8sided_dice=size_ENT/3
if (number_8sided_dice>int(number_8sided_dice)):    
    number_8sided_dice=int(number_8sided_dice)+1

rolls=read_roll(number_8sided_dice)

random_bit_string=""
for i in rolls:
    if   i =="8": random_bit_string += "000"
    elif i =="1": random_bit_string += "001"
    elif i =="2": random_bit_string += "010"
    elif i =="3": random_bit_string += "011"
    elif i =="4": random_bit_string += "100"
    elif i =="5": random_bit_string += "101"
    elif i =="6": random_bit_string += "110"
    elif i =="7": random_bit_string += "111"
    elif i ==" ": continue
    else        : print("error ",i)

random_bit_string=random_bit_string[:size_ENT]

random_byte_string=bits2bytes(random_bit_string)
hash=sha256(random_byte_string).digest()
bhash=''.join(format(byte, '08b') for byte in hash)
CS=bhash[:size_CS]
final_entropy=random_bit_string+CS

for t in range(number_of_words):    
    extracted_bits=final_entropy[11*t:11*(t+1)]
    word_index=int(extracted_bits,2)
    if t==0: words_extracted=     words[word_index]
    else:    words_extracted+=' '+words[word_index]
print (words_extracted)