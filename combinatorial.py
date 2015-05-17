# Given total and list of denominations
# list # of ways to add up to total
# runtime: O(n*m)

def make_change(amount, denominations) :
	tempArr = [0] * (amount+1)
	for coin in denominations :
		for total in range(coin, amount+1) :
			if total % coin == 0 : tempArr[total] += 1
			else :
				subTotal = total - coin
				tempArr[total] += tempArr[subTotal]
	print(tempArr)
	return tempArr[amount]

print make_change(4, [1,2,3])
print make_change(5, [1,3,5])
print make_change(5, [1,2,3])