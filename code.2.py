print("\nTask 2: Find positions of number in a list")
rand_nums = [random.randint(1, 10) for _ in range(20)]
print("Random List:", rand_nums)
target = int(input("Enter number to find positions: "))
positions = [i for i, num in enumerate(rand_nums) if num == target]
print("Positions of", target, "in list:", positions)
