phone_number = input('entrez un numérode téléphone : ')
temp=''
for ele in phone_number :
    if ele != ' ' :
        temp+=ele
phone_number=temp

print('')

def spell_phone_number(phnbr:str) :
    numbers = {
        '0' : "Zero",
        '1' : "One",
        '2' : "Two",
        '3' : "Three",
        '4' : "Four",
        '5' : "Five",
        '6' : "Six",
        '7' : "Seven",
        '8' : "Eight",
        '9' : "Nine",
    }

    for ele in phone_number : print(numbers[ele]+' ',end=' ')

spell_phone_number(phone_number)