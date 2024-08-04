def remove_occurrences(lst :list[int], num: int) -> list[int]:
    return [x for x in lst if x != num]
original_list = [1, 2, 3, 4, 2, 5, 2]
number_to_remove = 2
result = remove_occurrences(original_list, number_to_remove)
print(result)