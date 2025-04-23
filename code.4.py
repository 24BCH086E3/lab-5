print("\nTask 4: Separate positive and negative numbers")
rand_nums = [random.randint(-50, 50) for _ in range(30)]
pos_nums = [num for num in rand_nums if num > 0]
neg_nums = [num for num in rand_nums if num < 0]
print("Original List:", rand_nums)
print("Positive Numbers:", pos_nums)
print("Negative Numbers:", neg_nums)
