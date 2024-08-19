L=[1,2,3,3,4,4,5,5,6]

def elements(L):
    seen=set()
    unique_list=[]
    duplicates_list=[]
    for i in L:
        if i not in seen:
            unique_list.append(i)
            seen.add(i)
        else:
            duplicates_list.append(i)
    return unique_list,duplicates_list

unique_list, duplicates_list = elements(L)
print(f"Unique_Elements:{unique_list}")
print(f"Duplicate_Elements:{duplicates_list}")