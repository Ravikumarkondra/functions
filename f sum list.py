# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20 

def sum_numbers_in_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

sample_list = [8, 2, 3, 0, 7]
result = sum_numbers_in_list(sample_list)
print("sum of list: ", result)
