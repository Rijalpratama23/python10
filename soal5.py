# input :  [105, 20, 8, 150, 30, 5, 200]
# Output : [20, 30]

angka = [105, 20, 8, 150, 30, 5, 200]
output = []

for i in angka:
    if 10 <= i <= 100:
        output.append(i)

output.sort()
print(output)