try :
    with open('./course/data/poem.txt','r') as f:

        content = f.read()

except FileNotFoundError:
    content = None

print(content)

oceans = [
    "Pacific",
    "Atlantic",
    "Indian",
    "Southern",
    "Artic"
]

with open('./course/data/ocean.txt','w') as f :

    for key,ocean in enumerate(oceans) :
        f.write(ocean)
        if key+1!=len(oceans) :
            f.write('\n')