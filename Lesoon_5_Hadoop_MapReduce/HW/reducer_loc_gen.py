import sys 

lists = []
for line in sys.stdin: 
    words = line.strip().split('\n')

    for word in words:
        lists.append(word)

a = lists[0]
list_two = eval(a.strip("[]"))
b = lists[3]
list_one = eval(b.strip("[]"))

for i in range(len(list_one)):
    if list_one[i]['id_restaurant'] == 'NULL':
        pass
    else:
        for j in range(len(list_two)):
            if list_two[i]['id_restaurant'] == 'NULL':
                pass
            else:
                if list_one[i]['id_restaurant'] == list_two[j]['id_restaurant']:
                    list_one[i]['city'] = list_two[j]['city']
                    list_one[i]['label'] = list_two[j]['label']
                    list_one[i]['food_type'] = list_two[j]['food_type']
                    list_one[i]['review'] = list_two[j]['review']
                else:
                    pass

union_dict = []
for q in range(len(list_one)):
    if (list_one[q]['id_restaurant'] != 'NULL'):
        if  'label' in list_one[q].keys():
                union_dict.append(list_one[q])
        else: 
            pass

print(union_dict)

