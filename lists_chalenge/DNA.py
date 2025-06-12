# Write code below 💖

dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']

item_to_find = input("Enter DNA: ")
item_found = False

for i in dna_sequence:
    if i == item_to_find:
        item_found = True
        break

if item_found == True:
    print("Item Found!")
else:
    print("Item not found.")