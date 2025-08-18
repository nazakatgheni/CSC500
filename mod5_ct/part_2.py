# Part 2: Book Club Points Program (chained comparisons)

books = int(input("Enter the number of books purchased this month: "))

if books == 0:
    points = 0
elif 1 < books <= 3:      # 2–3 books
    points = 5
elif 3 < books <= 5:      # 4–5 books
    points = 15
elif 5 < books <= 7:      # 6–7 books
    points = 30
elif books >= 8:          # 8 or more
    points = 60
else:                     # covers books == 1 or invalid negatives
    points = 0

print(f"Books purchased: {books}")
print(f"Points earned: {points}")
