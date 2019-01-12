a = [3,6,2,8,6,5,7,4,9,1,0,3,4,5,7,3]
#a = [1,7,8,2,4]
b = len(a)
d = {2:6,6:9,5:4}
one = a[0]
two = a[1]
if (one > two):
    max = one
else:
    max = two
i = 2
while(i!=b):
    if (a[i]>max):
        max = a[i]
    i += 1

for k,v in d.items():
    if (v == max):
        print (k) 
print (max)    