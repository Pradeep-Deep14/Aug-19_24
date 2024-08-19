#Solution 1
my_list = [1, 2, 3, 4, 1, 2, 3, 5, 4, 5]
my_set = set(my_list)
my_unique_list = list(my_set)
print(my_unique_list)

#Solution 2

my_list = [1, 2, 3, 4, 1, 2, 3, 5, 4, 5]

def unique_elements(my_list):
    unique_elements=[]
    for i in my_list:
        if i not in unique_elements:
            unique_elements.append(i)
    return unique_elements

print(unique_elements(my_list))

#Print duplicates alone

my_list = [1, 2, 3, 4, 1, 2, 3, 5, 4, 5]

def duplicate_elements(my_list):
    seen=set()
    duplicate_elements=[]
    for i in my_list:
        if i in seen:
            duplicate_elements.append(i)
        seen.add(i)
    return  duplicate_elements
    
print(duplicate_elements(my_list))