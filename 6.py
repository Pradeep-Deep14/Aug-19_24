L1=[1,4,5,7,8,9,10,11,14]
L2=[]

def missed_elements(L1):
    for i in range(1,16):
        if i not in L1:
            L2.append(i)
    return L2

print(missed_elements(L1))