fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

#print(fruits[-2::-1])

for idx, fruit in enumerate(fruits[-2::-1]):
	print(fruit, idx, fruits[-1-idx:])
	
print("apple" in fruits)
print()
# print(fruits[-2::-1][0])
# for idx, fruit in enumerate(fruits[0:-1]):
# 	print(fruit, idx)