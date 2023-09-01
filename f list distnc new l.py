# 2.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def unique(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = unique(sample_list)
print("Sample List:", sample_list)
print("Unique List:", unique_list)

