print("Task 1: Create and modify lists")
odd_list = random.sample(range(1, 50, 2), 5)
even_list = random.sample(range(2, 50, 2), 4)
print("Odd list:", odd_list)
print("Even list:", even_list)

odd_list[2] = even_list  
print("Odd list after embedding even list at position 3:", odd_list)


flat_list = []
for item in odd_list:
    if isinstance(item, list):
        flat_list.extend(item)
    else:
        flat_list.append(item)

flat_list.sort()
print("Flattened and sorted list:", flat_list)
