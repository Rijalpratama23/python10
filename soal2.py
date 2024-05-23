# input [7,4,9,2,5,1]
# output [2,4]

a_int =[7,4,9,2,5,1]
keluar = []
for b in a_int:
    if b % 2 == 0:
        keluar.append(b)
keluar.sort()
print(keluar) 