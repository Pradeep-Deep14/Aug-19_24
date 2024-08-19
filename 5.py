L=[1,2,3,4,4,5,5,6,6,7,7,8,9]
duplicates=[]

def duplicates(L):
    for i in L:
        if i in duplicates:
            duplicates.append(i)
        return duplicates

print(duplicates(L))
