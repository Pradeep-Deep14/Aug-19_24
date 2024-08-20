my_list = [1, 2, 3, 4, 4]

unique_elements=len(list(set([x for x in my_list if my_list.count(x)==1])))
print(unique_elements)