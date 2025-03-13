import random
import string

no_of_dict = random.randint(2,10)
no_of_key_value_pair = random.randint(2,4)
dict_list =[]
for i in range(1,no_of_dict):
    dict_temp={}
    for j in range(0, no_of_key_value_pair):
        key = random.choice(string.ascii_lowercase)
        value = random.randint(0,100)
        dict_temp[key]=value
    dict_list.append(dict_temp)
final_dict={}
for i in dict_list:
    for key in i.keys():
        if key not in final_dict:
            final_dict[key]= i[key]
        else:
            if final_dict[key]<i[key]:
                final_dict[key]=i[key]
print(final_dict)


