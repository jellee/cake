# highest product of three integers in an array

def highest_product(array_of_ints) :
    if len(array_of_ints) < 3 : raise Exception("Less than 3 items!")

    maxNum = minNum = array_of_ints[0]
    maxTwo = minTwo = array_of_ints[0] * array_of_ints[1]
    maxProd = maxTwo * array_of_ints[2]

    if len(array_of_ints) == 3 : return maxProd

    # get max and min numbers
    if array_of_ints[0] <= array_of_ints[1] :
        maxNum = array_of_ints[1]
    else : minNum = array_of_ints[1]

    for item in array_of_ints[2:] :
        maxProd = max(maxTwo * item, minTwo * item, maxProd)
        maxTwo = max(maxTwo, item * maxNum, item * minNum)
        minTwo = min(minTwo, item * maxNum, item * minNum)
        maxNum = item if maxNum < item else maxNum
        minNum = item if minNum > item else minNum
    return maxProd

print highest_product([1,2,3,4,5])
print highest_product([3,6,3,2,0])
print highest_product([-10, -10, 2, 3, 5])
print highest_product([3,2,-10,5,-10])