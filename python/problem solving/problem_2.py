'''def find_duplicates(numbers):
    duplicates = []
    for num in numbers:
        if numbers.count(num) > 1:
            duplicates.append(num)
    return sorted(set(duplicates))

numbers = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 8]
print("Duplicates:", find_duplicates(numbers))
# Duplicates: [1, 2, 8]
# 
# 
# 
# '''




def find_duplicates(numbers):
    duplicates = []
    for num in numbers:
        if numbers.count(num) > 1:
            duplicates.append(num)
    return sorted(set(duplicates))

numbers = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 8]
print("Duplicates:", find_duplicates(numbers))
