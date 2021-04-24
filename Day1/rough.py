a = [5, 1, 2, 3]

j = 0
n2 = 4
temp = a[j]
k = j+1
while(k < n2 and a[k] < temp):
    a[k-1] = a[k]
    k += 1
a[k-1] = temp

print(a)
