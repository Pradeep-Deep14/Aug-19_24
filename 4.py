#Nested list to flattened list

List=[[1,2],[3,4,5,5],[6,6,7,8]]
flattened=[]

def flattened_list(List):
    for sublist in List:
        for i in sublist:
            if i not in flattened:
                flattened.append(i)
    return flattened

print(flattened_list(List))