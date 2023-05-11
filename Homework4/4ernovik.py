array: list[list[int]] = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
result_list =[]
for h_list in array:
    result_list += h_list
result_list.sort()
print(result_list)