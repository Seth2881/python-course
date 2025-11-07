text = 'Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stoodAnd looked down one as far as I could To where it bent in the undergrowth.'.lower()

def idk_how_to_name_it(strzone:str) :
    letter_dict = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

    for key in letter_dict :
        letter_dict[key] = strzone.count(key)
    
    return letter_dict

print(idk_how_to_name_it(text))