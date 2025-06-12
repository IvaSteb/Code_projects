bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]

total = 0

for i in bill:
    total = total + i

new_total = total / 4
print(f"Every of 4 friends may to pay {new_total}")