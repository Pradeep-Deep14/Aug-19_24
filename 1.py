List=[1,2,2,3,3,4,5]
List1=[]

def duplicates(List):
    for i in List:
        if i not in List1:
            List1.append(i)
    return List1

print(duplicates(List))