def count_unique_elements(L):
    unique_elements = []
    for item in L:
        if item not in unique_elements:
            unique_elements.append(item)
    return len(unique_elements)

# Example usage
L = [1, 2, 'abc', 2, 66, 'abc', 66, 66, 99, 'abc']
unique_count = count_unique_elements(L)

print("Total count of unique elements:", unique_count)
