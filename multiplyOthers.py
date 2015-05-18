# find the product of all other numbers in the array
# runtime: O(n)

def multiply_all_others (intArray) :
	n = len(intArray)
	prodArray = [1] * n
	for i in range(n) :
		tempVal = prodArray[i]
		prodArray = [intArray[i] * item for item in prodArray]
		prodArray[i] = tempVal
	return prodArray

print(multiply_all_others([1,7,3,4]))