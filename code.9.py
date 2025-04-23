print("\nTask 9: List difference using list comprehension")
list1 = [random.randint(1, 20) for _ in range(10)]
list2 = [random.randint(1, 20) for _ in range(10)]
list3 = [x for x in list1 if x not in list2]
print("List 1:", list1)
print("List 2:", list2)
print("Difference (in list1 but not in list2):", list3)
