from cesar_coding import decode,cesar_coding

key = 'TXAZCELYE'
key_possibilities = decode(key)
fichier = open('key.txt','r')
for ligne in fichier :
    message = ligne
fichier.close()

def xor(key:str,caracter:str) :
    a = str(bin(ord(key)))[2:]
    b = str(bin(ord(caracter)))[2:]
    xored_value = ''

    for i in range(len(a)) :
        if a[i] == b[i] :
            xored_value += '0'
        else :
            xored_value += '1'

    return xored_value

def decrypt(keys:list[str],text:str)->list[str] :
    list_car = []
    for i in range(len(text)) :
        list_car.append(xor(keys[i%len(keys)],text[i]))
    return list_car

print(decrypt(message))