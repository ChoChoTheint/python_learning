mylist = []
mylist.append(1)
mylist.append('two')
mylist.append(3.0)

for x in mylist:
    print(x)

mylist = [1,2,3,4]
try:
    print(mylist[7])
except:
    print('good thing I caught this exception')

print([1,2,3] * 10)

even = [2,4,6,8]
odd = [1,3,5,7]
print(even + odd)

a = b = c = [1]
b.append(2)
print(a, b, c)

a, b, c = 1, 2, 3
print(a, b, c)