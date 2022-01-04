dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict_two = {'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 0}

# for key in dict_two:                 # dict_one.update(dict_two)
#     dict_one[key] = dict_two[key]  

# print(dict_one)
for i in dict_two:
    dict_one[i]=dict_two[i]
print(dict_one)

