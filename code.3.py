print("\nTask 3: Remove duplicates from random list")
rand_nums = [random.randint(1, 30) for _ in range(50)]
print("Original List:", rand_nums)
unique_nums = list(set(rand_nums))
print("List after removing duplicates:", unique_nums)
