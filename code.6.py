print("\nTask 6: Fahrenheit to Celsius conversion")
f_temps = [random.randint(60, 100) for _ in range(10)]
c_temps = [round((f - 32) * 5/9, 2) for f in f_temps]
print("Fahrenheit:", f_temps)
print("Celsius:", c_temps)
