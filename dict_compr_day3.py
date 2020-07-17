# dict_abs = {'a':1, 'b':2, 'c':3, 'd':3}

# dict_123 = {value: key for key, value in dict_abs.items()}
# print(dict_123)

# my_dict = {key:value**2 for key , value in dict_abs.items()}
# print(my_dict)

# my_dict = {key: dict_abs[key]**2 for key in dict_abs.keys()}
# print(my_dict)

my_dict = {'a':1, 'b':2, 'c':3, 'd':-4, 'e':-5}
new_dict = {key: value for key, value in my_dict.items() if value >0}
print(new_dict)


# my_dict = {'a':1, 'b':2, 'c':3, 'd':-4, 'e':-5}
# new_dict = {key: value for key, value in my_dict.items() if value <0 and key != 'e'}
# print(new_dict)

#  my_dict = {'a':1, 'b':2, 'c':3, 'd':-4, 'e':-5}
#  new_dict = {val for key, val in my_dict.items() if val < 0 and key != 'e'}
#  print(new_dict)



############################################SET

# list_a = [-2, -1, 0, 1, 2, 3, 4, 5, 2, 3, -2]
# my_set = {i for i in list_a}
# print(my_set)