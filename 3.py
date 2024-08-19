L = [1, [2, 3], [4, 5, 6], [6, 7, 7]]
flattened = []

def flattened_list(L):
    for sublist in L:
        if isinstance(sublist, list):  # Check if the item is a list
            for i in sublist:
                if i not in flattened:
                    flattened.append(i)
        else:
            if sublist not in flattened:  # Handle non-list items
                flattened.append(sublist)
    return flattened

print(flattened_list(L))
