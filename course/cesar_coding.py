from random import randint as rand
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def cesar_coding(nbr:int)->str :
    '''
    Generate the "rolled" alphabet that is used to encode a prompt
    '''
    alphabet_cesar = ''
    for i in range(1,27) :
        if (i+nbr)%26+96 == 96:
            alphabet_cesar+='z'
        else :
            alphabet_cesar+=chr((i+nbr)%26+96)

    return alphabet_cesar



def decode(prompt:str)->list[str]:
    '''
    decode a message with the 25 possible rolled alphabet generated with cesar_coding()
    '''
    global alphabet
    encode_alphabet = []
    for i in range(1,27):
        encode_alphabet.append(cesar_coding(i))
    temp_var = ''
    return_str = []

    for ceasar_alphabet in encode_alphabet:
        for char in prompt:
            if char.lower() in alphabet :
                i = ceasar_alphabet.index(char.lower())
                if char.isupper() :
                    temp_var += alphabet[i].upper()
                else :
                    temp_var += alphabet[i]
            else :
                temp_var += char
        return_str.append(temp_var)
        temp_var = ''

    return return_str



def encode(prompt:str,nbr:int)->str:
    '''
    encode a prompt with a specific rolled alphabet generated with cesar_coding()
    '''
    global alphabet
    encode_alphabet = cesar_coding(nbr)
    return_str = ''

    for char in prompt:
        if char.lower() in alphabet :
            i = alphabet.index(char.lower())
            if char.isupper() :
                return_str += encode_alphabet[i].upper()
            else :
                return_str += encode_alphabet[i]
        else :
            return_str += char

    return return_str

fichier = open('course/caesar_decoded_possibilities/decoded.txt','w')

prompt = "Attention Minecraft c'est cool, mais c'est chronophage. . ."
crypted = encode(prompt,rand(1,26))
decrypted = decode(crypted)

print('prompt :',prompt)
print()
print('encoded messages :',crypted)
print()
for elem in decrypted :
    fichier.write(elem+'\n')
fichier.close()
print('Decrypted possibilities saved in course/caesar_decoded_possibilities/decoded.txt')