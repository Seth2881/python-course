# 1. Calculer une réduction de 15% des prix de la liste suivante
# INPUT : prices = ['95,62€', '11,61€', '100,50€', '62,33€']
# OUTPUT : prices_discounted ...

#EXO 1
def format_change(amount:str)->float:
    return float(amount[:-1].replace(',','.'))

def format_change_into_str(amount:float)->str:
    amount = str(amount).split('.')
    return amount[0]+','+amount[1]+'€'

def discount(amount:str)->str:
    amount = format_change(amount)
    #discount de 15%
    amount = round(amount*0.85,2)
    return format_change_into_str(amount)

list_price = ['95,62€', '11,61€', '100,50€', '62,33€']
list_prices_discounted = []
for price in list_price :
    list_prices_discounted.append(discount(price))
print(list_prices_discounted)

# 2. Extraire le nom et le prénom de chacun des mails suivants
# INPUT : emails = ['pierre.dupont@yahoo.fr', 'marie.curie@gmail.com']
# OUTPUT : 
"""
users = [
    {
        'first_name': 'pierre', 
        'last_name': 'dupont'
    },    
    {
        'first_name': 'marie', 
        'last_name': 'curie'
    },
]
"""

#EXO 2

def find_name_surname(email:str)->dict:
    return {
        'first_name' : email.replace('@','.').split('.')[0],
        'last_name' : email.replace('@','.').split('.')[1]
    }

emails = ['pierre.dupont@yahoo.fr', 'marie.curie@gmail.com']
list_name = []

for email in emails :
    list_name.append(find_name_surname(email))
print(list_name)

# 3. Supprimer de la liste les fruits qui finit par une voyelle
# INPUT : fruits = ['Apple', 'Cherry', 'Mandarin', 'Banana', 'Pear']
# OUTPUT : fruits = ['Mandarin', 'Pear']

#EXO 3

def fruct_select(fructs:list[str])->list[str]:
    for fruct in fructs :
        if fruct[-1] in 'aeiouy' :
            while fruct in fructs :
                fructs.remove(fruct)
    return fructs

fruits = ['Apple', 'Cherry', 'Mandarin', 'Banana', 'Pear']
print(fruct_select(fruits))

# 4. Faire une fonction appelée "words_count" qui compte les mots d'un texte en entrée
# INPUT : sentence = "J'adore la langage de programmation Python"
# OUTPUT : 7

#EXO 4

def words_count(text:str)->int:
    return len(text.replace("'",' ').split(' '))

sentence = "J'adore la langage de programmation Python"
print(words_count(sentence))

# 5. Faire une fonction appelée "get_largest_gap"
# qui retourne l'écart entre la note la plus basse et la meilleure note
# INPUT : marks = [8, 17.5, 6, 11, 15]
# OUTPUT : 11.5   (17.5 - 6)

#EXO 5

def get_largest_gap(marks:list[float])->float:
    return max(marks)-min(marks)

marks = [8, 17.5, 6, 11, 15]
print(get_largest_gap(marks))

# 6. Faire une fonction appelée "get_ages_average" 
# qui calcule la moyenne d'âges des utilisateurs.
# INPUT : 
"""
users = [
    {
        'first_name': 'pierre', 
        'last_name': 'dupont',
        'age': 42
    },    
    {
        'first_name': 'marie', 
        'last_name': 'curie',
        'age': 18
    },
    {
        'first_name': 'marie', 
        'last_name': 'curie',
        'age': 35
    },
]
"""
# OUTPUT : ages_average = 71.67   ((42+18+35) / 3)

#EXO 6

def get_age_average(users:list[dict])->float :
    age_average = 0
    for user in users :
        age_average += user['age']
    return round(age_average/len(users),2)

users = [
    {
        'first_name': 'pierre', 
        'last_name': 'dupont',
        'age': 42
    },    
    {
        'first_name': 'marie', 
        'last_name': 'curie',
        'age': 18
    },
    {
        'first_name': 'marie', 
        'last_name': 'curie',
        'age': 35
    },
]

print(get_age_average(users))

