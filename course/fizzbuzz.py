def fizzbuzz(ctn:int)->None :
    for nbr in range(1,ctn+1) :
        if nbr%3==0 :
            prompt = 'Fizz'
        if nbr%5==0 :
            prompt += ' Buzz'
        elif nbr%3!=0 and nbr%5!=0 :
            prompt = f'{nbr}'
        print(prompt.strip())
        prompt=''

fizzbuzz(16)