fruit = ["apel", "jeruk", "mangga"]
fruit2 = ["apel", "anggur", "nanas"]
output = []
fruit.extend(fruit2)

for i in fruit:
    if i not in output:
        output.append(i)

output.sort()
print(output)