import sys 

lists = []
for line in sys.stdin: 
    words = line.strip().split('\n')

    for word in words:
        lists.append(word)


a = lists[0]
list_one = eval(a.strip("[]"))
b = lists[3]
list_two = eval(b.strip("[]"))


for i in range(len(list_one)):
    if list_one[i]['city'] == 'NULL':
        pass
    else:
        for j in range(len(list_two)):
            if list_two[i]['city'] == 'NULL':
                pass
            else:
                if list_one[i]['city'] == list_two[j]['city']:
                    list_one[i]['id_restaurant'] = list_two[j]['id_restaurant']
                    list_one[i]['street_num'] = list_two[j]['street_num']
                    list_one[i]['street_name'] = list_two[j]['street_name']
                else:
                    pass
                
union_dict = []
for q in range(len(list_one)):
    if (list_one[q]['city'] != 'NULL'):
        if  'id_restaurant' in list_one[q].keys():
            union_dict.append(list_one[q])

    else:
        pass

print(union_dict)