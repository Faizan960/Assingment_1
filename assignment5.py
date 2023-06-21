
print(" Sum() ")

lst2 = [1,2,3,4,5,10,9,7,8,6]
print(sum(lst2))

print(" Min() ")

print(min(lst2))

print(" Max() ")

print(max(lst2))

print(" Sort()In Ascending Default ")

lst2.sort()
print(lst2)

print(" Sort()In Descending ")

lst2.sort(reverse=True)
print(lst2)

print(" Conversion Of List Into Tuple ")

t1=tuple(lst2)
print("list : ",lst2)
print("tuple: ",t1)

print(" Delete Or Deletion ")

lst2.__delitem__(1)
print(lst2)