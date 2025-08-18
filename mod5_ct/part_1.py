# Rainfall Average (simple + clear)

years = int(input("How many years of data? (enter a count like 1–10): "))
while years < 1 or years > 10:
    years = int(input("Please enter a number between 1 and 10: "))

total_rainfall = 0.0
total_months = years * 12

for y in range(1, years + 1):
    print(f"\nYear {y}:")
    for m in range(1, 13):
        r = float(input(f"  Inches of rainfall for month {m}: "))
        while r < 0:
            r = float(input("    Non-negative only. Try again: "))
        total_rainfall += r

average = total_rainfall / total_months

print("\nRainfall Statistics")
print("-------------------")
print(f"Total months: {total_months}")
print(f"Total rainfall: {total_rainfall:.2f} inches")
print(f"Average rainfall per month: {average:.2f} inches")
