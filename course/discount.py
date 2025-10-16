prices = ['24,99€', '12,75€', '9,99€']
# def formatChange(price:str) :
#     temp = price.replace(',','.')
#     temp1 = temp.replace('€','')
#     return float(temp1)

# def oldFormat(price:str) :
#     temp = price.replace('.',',')
#     temp += '€'
#     return str(temp)

# def discount(list_price) :
#     temp = []
#     for ele in list_price :
#         temp.append(oldFormat(str(round(formatChange(ele)*0.85,2))))
#     return temp

# print(discount(prices))
print([f'{round(float(ele.replace(',', '.').replace('€', '')) * 0.85, 2)}€'.replace('.',',') for ele in ['24,99€', '12,75€', '9,99€']])