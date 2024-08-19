#Solution 1
L=[1,2,3,4,5]
L.reverse()
print(L)

#Solution 2


L=[1,2,3,4,5]

def reversed_list(L):
    my_list=[]
    for i in L:
        my_list.insert(0,i)
    return my_list

print(reversed_list(L))

#Solution 3

L=[1,2,3,4,5]
L1=[]
for i in range(len(L)-1,-1,-1):
    L1.append(L[i])

print(L1)

#Solution 4

L=[1,2,3,4,5]
L1=list(reversed(L))
print(L1)