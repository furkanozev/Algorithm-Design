"""
	Furkan OZEV
		161044036
			"""

import random 

def part1(row):

	i = 1
	n = (len(row) // 2)
	j = 0

	if (n%2 == 0):
		j = n
	else:
		j = n + 1

	while i < n:
		blackbox = row[i]
		whitebox = row[i + n]
		row[j] = blackbox
		row[i] = whitebox
		i += 2
		j += 2


def part2(coinlist):

	length = len(coinlist)

	if (length % 2 == 0):
		sum1 = sum(coinlist[0:length//2])
		sum2 = sum(coinlist[length//2:length])
		if (sum1 > sum2):
			return part2(coinlist[length//2:length])  + length//2
		else:
			return part2(coinlist[0:length//2])
	else:
		sum1 = sum(coinlist[0:(length-1)//2])
		sum2 = sum(coinlist[(length+1)//2:length])
		if (sum1 > sum2):
			return part2(coinlist[(length+1)//2:length]) + (length+1)//2
		elif (sum2 > sum1):
			return part2(coinlist[0:(length-1)//2])
		else:
			return (length-1)//2


def part3_quickSort(arr, low, high):

	swap = 0
	if low < high: 
		i = low - 1
		pivot = arr[high]

		for j in range(low, high): 
			if (arr[j] < pivot): 
				i = i+1 
				arr[i],arr[j] = arr[j],arr[i]
				swap += 1

		arr[i+1], arr[high] = arr[high], arr[i+1] 
		swap += 1
		i += 1
		swap += part3_quickSort(arr, low, i-1)
		swap += part3_quickSort(arr, i+1, high)
	
	return swap


def part3_insertionSort(arr): 

	length = len(arr)
	swap = 0

	for i in range(1, length):
		j = i-1
		current = arr[i]

		while (j >= 0 and current < arr[j]):
			arr[j + 1], arr[j] = arr[j], current
			swap += 1
			j -= 1

	return swap


def part4(arr):

	n = len(arr)

	if(n % 2 == 0):
		arr2 = arr[ : ]
		return (part4_helper_kthlargest(arr, n//2) + part4_helper_kthlargest(arr2, n//2 + 1)) / 2.0
	else:
		return part4_helper_kthlargest(arr, n//2 + 1)


def part4_helper_kthlargest(arr, k):

	low = 0
	high = len(arr) - 1

	index = low - 1
	pivot = arr[high]

	for j in range(low, high):
		if (arr[j] <= pivot):
			index = index + 1
			arr[index], arr[j] = arr[j], arr[index]

	arr[index + 1], arr[high] = arr[high], arr[index + 1]
	index += 1

	if index == (high - k + 1):
		result = arr[index]
	elif index > (high - k + 1):
		result = part4_helper_kthlargest(arr[ : index], k - (high - index + 1))
	else:
		result = part4_helper_kthlargest(arr[index + 1 : high + 1], k)
    
	return result


def part5(arr, index = 0, subarr = [], result = []):

	if index == len(arr):
		if len(subarr) != 0:
			result = part5_helper_check(arr, result, subarr)
	else:
		# Recursive Part
		result1 = part5(arr, index + 1, subarr, result)
		result2 = part5(arr, index + 1, subarr+[arr[index]], result)
		
		if(len(result1) == 0):
			result = result2
		elif(len(result2) == 0):
			result = result1
		else:
			result = part5_helper_check(arr, result1, result2)

	return result

def part5_helper_check(arr, oldsub, newsub):

	n = len(arr)
	maxelem = max(arr)
	minelem = min(arr)
	cond = (maxelem + minelem) * n / 4.0
	sumarr = sum(newsub)

	if(sumarr >= cond):
		mult1 = part5_helper_multiply(oldsub)
		mult2 = part5_helper_multiply(newsub)

		if(len(oldsub) == 0):
			return newsub
		elif(mult1 > mult2):
			return newsub

	return oldsub

def part5_helper_multiply(arr):

	if(len(arr) == 0):
		result = 0
	else:
		result = 1
		for x in arr:
			result = result * x

	return result     


def driver1():
	print("-------------- PART1 TEST --------------")

	row = list()
	n = random.randint(1,20)

	row.extend(["Black" for i in range(n)])
	row.extend(["White" for i in range(n)])

	print("\nROW: ({} elements => first {} boxes are black and last {} boxes are white)\n{}\n".format(2*n, n, n, row))
	print("\t--- AFTER ALGORITHM ---")
	part1(row)
	print("ROW:\n{}\n".format(row))
	print("----------------------------------------\n")


def driver2():
	print("-------------- PART2 TEST --------------")

	coinlist = list()
	n = random.randint(3,20)
	realcoinweight = random.randint(2,200)
	fakecoinweight = random.randint(1,realcoinweight-1)
	fakecoinindex = random.randint(0,n-1)

	coinlist.extend([realcoinweight for i in range(n)])
	coinlist[fakecoinindex] = fakecoinweight

	print("\nThere are {} coins.\n\tReal coins weight: {}\n\tFake coin weight: {}".format(n, realcoinweight, fakecoinweight))
	print("\nCoin weight list:\n{}\n".format(coinlist))
	print("\t--- AFTER ALGORITHM ---")
	result = part2(coinlist)
	print("Fake coin index: {}\t Face coin weight: {}\n".format(result, coinlist[result]))
	print("----------------------------------------\n")


def driver3():
	print("-------------- PART3 TEST --------------")

	arr = list()
	n = random.randint(3,20)
	arr.extend([random.randint(1,100) for i in range(n)])
	arr2 = arr[:]

	print("\nUnsorted Array:\n{}\n".format(arr))
	print("\t--- AFTER QUICKSORT ALGORITHM ---")
	swapquick = part3_quickSort(arr, 0, n-1)
	print("Sorted Array:\n{}".format(arr))
	print("Number of Swap: {}".format(swapquick))
	print("\n\t--- AFTER INSERTIONSORT ALGORITHM ---")
	swapquick = part3_insertionSort(arr2)
	print("Sorted Array:\n{}".format(arr2))
	print("Number of Swap: {}\n".format(swapquick))
	print("----------------------------------------\n")


def driver4():
	print("-------------- PART4 TEST --------------")

	arr = list()
	n = random.randint(1,20)
	arr.extend([random.randint(1,100) for i in range(n)])

	print("\nArray:\n{}\n".format(arr))
	print("\t--- AFTER ALGORITHM ---")
	result = part4(arr)
	print("Median of Array: {}\n".format(result))
	print("----------------------------------------\n")


def driver5():
	print("-------------- PART5 TEST --------------")

	arr = list()
	n = random.randint(6,15)
	arr.extend([random.randint(1,30) for i in range(n)])

	print("\nArray:\n{}\n".format(arr))
	print("\t--- AFTER ALGORITHM ---")
	result = part5(arr)
	if(len(result) == 0):
		print("There is no subset that satisfies these conditions.")
	else:
		print("Result Subarray:\n{}\n".format(result))
	print("----------------------------------------\n")


if __name__ == "__main__":

	print("\n!!! Every time the program runs, all test cases are randomly generated. !!!\n")

	driver1()
	driver2()
	driver3()
	driver4()
	driver5()

	print("\tAll tests finished.\n")