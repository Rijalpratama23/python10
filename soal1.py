# input [8,3,12,4,7,2]
# output [12,8,7,0,0,0]

arr = [8,3,12,4,7,2]
output = []
for a in arr:
    if a <=5 :
        output.append(0)
    else :
        output.append(a)  

output.sort(reverse=True)
print(output)