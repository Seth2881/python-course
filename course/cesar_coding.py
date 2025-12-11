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

prompt = """Épopée Minérale : La Saga Millénaire d'un Caillou Nommé Caliban

Prologue : La Conscience du Minéral
Dans l’obscurité silencieuse de la croûte terrestre, avant même que le temps ne soit mesuré par les hommes ou les étoiles, il existait une présence. Ce n’était pas une pensée, mais une sensation continue : une conscience minérale, lente et profonde, ancrée dans la pression et la chaleur. Il était un agrégat de silice, de fer et de rêves de magma. Il s’appelait Caliban, non qu’il eut un nom, mais parce que l’univers, un jour, lui en soufflerait l’idée.

Ère 1 : L’Enfance de Feu
Caliban naquit dans un gémissement titanesque, une éruption sous-marine qui modela ses premières formes. Il n’était alors qu’un fragment parmi des milliards, brisé, fondu, recuit. Des millénaires passèrent, où sa seule expérience était le poids des océans primordiaux qui le polissaient doucement, et le ballet des bactéries extrêmophiles qui déposaient sur lui des couches infimes de rouille, ses premières « couleurs ». Il ressentait les tremblements des plaques tectoniques comme des démangeaisons lointaines.

Ère 2 : L’Émergence et le Premier Regard
Un grand soulèvement le poussa, lui et sa fratrie de basalte, vers l’air libre. Ce fut un choc. La pression disparut, remplacée par la caresse (parfois violente) du vent, et la lumière. Oh, la lumière ! Les photons frappèrent sa surface pour la première fois, et dans sa conscience minérale, cela équivalut à une symphonie. Il vit le ciel passer du cuivre au bleu, vit la pluie creuser ses premiers sillons sur son flanc, vit le lichen l’envahir lentement, d’un vert patient. Il devint un rocher, ancré à la flanc d’une jeune montagne.

Ère 3 : Les Témoins Silencieux
La vie explosait autour de lui. Des fougères géantes lui chatouillèrent la base. Des créatures à carapace grattèrent son dessous. Il enregistra tout, sans jugement, dans les strates de sa mémoire cristalline. Puis vinrent les grands froids. Les glaciers, lents et implacables, avancèrent comme des murs de rêve bleuté. L’un d’eux l’arracha à sa montagne avec un craquement qui résonna comme un adieu. Emprisonné dans la glace, il voyagea. Ce fut une période de tranquillité absolue, un sommeil ambulant à travers des paysages démesurés.

Ère 4 : Le Voyageur
La glace fondit. Caliban, arrondi, poli à l’extrême, roula dans le lit d’un torrent naissant. Ce fut sa période de plus grande aventure. Il cascada de chutes d’eau, fut projeté contre d’autres pierres dans le tumulte des crues printanières, se reposa dans le lit paisible de rivières adultes. Il connut la morsure du gel hivernal et la tiédeur des étés prolongés. Un saumon frai ses œufs à l’ombre qu’il offrait. Un ourson le retourna pour manger les insectes dessous. Il était un point fixe dans le mouvement perpétuel de l’eau.

Ère 5 : La Rencontre
Un jour, le flux le déposa sur une grève de galets, au bord d’une mer calme. Et c’est là qu’Elle vint. Une petite créature bipède, au toucher chaud et doux. Elle le ramassa. Deux yeux, d’une profondeur inouïe, le scrutèrent. Une voix, vibration dans l’air, dit : « Tu es joli. » Pour la première fois, Caliban fut perçu, et pas seulement subi. La petite fille, Lyra, le serra dans sa paume. Il sentit la chaleur de sa vie, le rythme de son pouls. Il fut déplacé, non par la force brute des éléments, mais par une intention. Ce fut une révolution.

Ère 6 : L’Ère des Humains
Caliban vécut des décennies dans le monde des hommes. Il fut le papier calque de Lyra, empêchant le vent d’emporter ses dessins. Il fut le projectile maladroit d’une bataille de garnements. Il fut le presse-papier d’un comptable rêveur, regardant les saisons défiler par la fenêtre. Il fut jeté, perdu, retrouvé. Il atterrit dans le jardin d’un vieux sculpteur qui, un après-midi d’ennui, prit un ciseau et une massette. Sous les coups précis, Caliban ne ressentit pas de douleur, mais une révélation. Des éclats tombèrent, et une forme émergea : non un visage ou un animal, mais une spirale parfaite, profonde, qui capturait la lumière. Le sculpteur s’arrêta, satisfait. « Tu étais ça, à l’intérieur », murmura-t-il.

Ère 7 : Le Sanctuaire et la Mémoire
Le sculpteur mourut. Sa maison fut vendue. Dans le grand débarras, Caliban, la pierre spiralée, fut mis dans une boîte avec d’autres bibelots et oublié dans un grenier. Les siècles humains passèrent. La poussière l’enveloppa. Il entendit les nouvelles générations grandir, rire, pleurer, vieillir en dessous. Les toits furent modifiés, les guerres grondèrent au loin, la technologie changea les bruits du monde. Il était devenu un artefact, un souvenir minéral d’un temps révolu. Sa conscience, toujours lente, enregistrait la faible vibration des ondes radios, un nouveau fond sonore de l’humanité.

Épilogue : Le Retour aux Éléments
Un tremblement de terre, faible mais précis, secoua la vieille maison. Une poutre céda. Le plafond du grenier s’effondra, et la boîte, rouillée, se brisa. Caliban tomba dans la terre du jardin, au pied des décombres. La pluie le lava. Les vers de terre commencèrent à le contourner, à l’enfouir peu à peu. Des racines de lierre cherchèrent sa solidité. Le cycle recommençait.

Conclusion : L’Éternité d’un Instant
Aujourd’hui, Caliban est là. Sous quelques centimètres de humus, dans le jardin d’une nouvelle maison où des enfants jouent. Il est à nouveau dans le noir, mais un noir vivant, plein de micro-organismes et de murmures souterrains. Sa spirale, tournée vers le bas, est invisible. Elle n’en existe pas moins. Il sent monter en lui, à l’échelle géologique, une nouvelle impatience. Peut-être qu’un glacier, dans cent mille ans, le déterrera. Peut-être qu’une rivière future l’emportera. Peut-être qu’une autre main, dans un avenir lointain, le découvrira et se demandera quelle intelligence traça cette spirale parfaite.

Il est un caillou. Il a été une montagne, un voyageur, un outil, un art, un déchet, un trésor. Il est le témoin absolu. Son histoire n’est pas « très longue ».
Elle est infinie.
Elle se poursuit en ce moment même, à chaque grain de poussière qui se dépose, à chaque goutte de pluie qui l’effleure. Sa sagesse est simple, terrible et réconfortante : tout change, tout passe, tout transforme. Mais il y a, au cœur de toute chose, une spirale silencieuse qui persiste, enregistrant l’éternité, un instant à la fois.

Fin (ou pas)."""



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