import random

def part1_b (arr):

	m = len(arr)
	n = len(arr[0])

	while True:
		count = 0
		temp1 = 0
		temp2 = 0
		res = 0

		for i in range(m):
			for k in range(i+1, m):
				for j in range(n):
					for l in range(j+1, n):
						if not (arr[i][j] + arr[k][l] <= arr[i][l] + arr[k][j]):
							temp1 = i
							temp2 = l
							count += 1
							res = arr[i][j] + arr[k][l] - arr[k][j]
							break
					if count > 0:
					    break
		if count == 1:
			arr[temp1][temp2] = res
		else:
			return arr


def part1_c_helper(arr):
    
    x = arr[0]
    for i in arr:
        if i < x:
            x = i
    return x

def part1_c(arr):
    
    length = len(arr)
    if(length == 1):
        res = list()
        res.append(part1_c_helper(arr[0]))
        return res
    
    indexlist = list()
    mid = length // 2
    indexlist += part1_c(arr[ :mid])
    indexlist += part1_c(arr[mid : ])
    return indexlist
arr = [[37, 23, 22, 32], [21, 6, 7, 10], [53, 34, 30, 31], [32, 13, 9, 6], [43, 21, 15, 8]]


def part2 (arr1, arr2, k):

	if len(arr1) == 0:
		return arr2[k]
	if len(arr2) == 0:
		return arr1[k]

	mid1 = len(arr1) // 2
	mid2 = len(arr2) // 2

	# If k is bigger than the sum of arr1 and arr2's median 
	if mid1 + mid2 < k:
		# If arr1's median is bigger than arr2's
		if arr1[mid1] > arr2[mid2]:
			# Arr2's first half doesn't include k th element
			return part2(arr1, arr2[mid2 + 1:], k - mid2 - 1)
		else:
			# Arr1's first half doesn't include k th element
			return part2(arr1[mid1 + 1:], arr2, k - mid1 - 1)
	# k is smaller than the sum of arr1 and arr2's 
	else:
		# If arr1's median is bigger than arr2's
		if arr1[mid1] > arr2[mid2]:
			# Arr1's second half doesn't include k th element
			return part2(arr1[:mid1], arr2, k)
		else:
			# Arr2’s second half doesn’t include k th element
			return part2(arr1, arr2[:mid2], k)


def part3(arr):

	if len(arr) == 0:
		return None

	# Returns the lower and higher indexes of the subset
	l, h = part3_helper(arr, 0, len(arr) - 1)
	return arr[l:h+1]

def part3_helper(arr, l, h):
	# Return the subset boundary to low and high indexes
	if l == h:
		return (l, h)

	mid = (l + h) // 2

	# Recursively get the left and right largest sum of the contiguous subset
	leftLargest = part3_helper(arr, l, mid)
	rightLargest = part3_helper(arr, mid + 1, h)
	# Merge and return it
	return part3_helper2(arr, leftLargest, rightLargest)

def part3_helper2(arr, l, r):
	# Merge left and right subsets
	# Calculate the sum of left part
	l_l, l_r = l[0], l[1]
	leftSum = sum(arr[l_l : l_r + 1])

	# Calculate the sum of right part
	r_l, r_r = r[0], r[1]
	rightSum = sum(arr[r_l : r_r + 1])
	# If left and right subsets are adjacent
	if (r_l - l_r) == 1:
		# Calculate the both subset sum
		l_rSum = leftSum + rightSum

		if (leftSum <= l_rSum) and (rightSum <= l_rSum):
			# Return low from left subset, high from right subset.
			return (l_l, r_r)

	else:
		# Calculate the sum of range
		ranges = sum(arr[l_l : r_r + 1])

		if (leftSum <= ranges) and (rightSum <= ranges):
			# Return low and high indexes
			return (l_l, r_r)
	# Return the subset that has largest sum
	if leftSum < rightSum:
		return r
	else:
		return l


def part4(graph, src = 0):
# If graph is Bipartite, returns true. Else return false.
	vertex = len(graph)
	# Create color array to store colors.
	# Vertex number is used as index in this array.
	# The value '-1' in colorArr[i] is used to specify no color is assigned to vertex 'i'.
	arrColor = [-1] * vertex

	# The value 1 is used to indicate first color is assigned and value 0 indicates second color is assigned.
	# Assign first color to source 
	arrColor[src] = 1
	# Create a queue of vertex numbers
	queue = list()
	queue.append(src)

	# While there are vertices in queue
	while queue:
		u = queue.pop()
		# Return false if there is a self-loop
		if graph[u][u] == 1: 
			return False

		for v in range(vertex):
			# If an edge from u to v exists and destination v is not colored.
			if (graph[u][v] == 1) and (arrColor[v] == -1):
				# Assign alternate color to this adjacent v of u. 
				arrColor[v] = 1 - arrColor[u]
				queue.append(v) 
			# An edge from u to v exists and destination v is colored with same color as u.
			elif (graph[u][v] == 1) and (arrColor[v] == arrColor[u]): 
				return False
	return True


def part5(cost, price):


	cost = cost[:-1]
	price = price[1:]
	day = 1

	res = list(part5_helper(cost, price, day))

	if res[0] > 0:
		res.insert(0, True)
	else:
		res.insert(0, False)

	return res

def part5_helper(cost, price, day):

	if len(cost) == 1:
		gain = price[0] - cost[0]
		return (gain, day)
	else:	
		res1 = part5_helper(cost[:1], price[:1], day)
		res2 = part5_helper(cost[1:], price[1:], day+1)

		if res1[0] > res2[0]:
			return res1
		else:
			return res2

def driver1():
	print("-------------- PART1_B TEST --------------")

	arr = [[37, 23, 22, 32], [21, 6, 7, 10], [53, 34, 30, 31], [32, 13, 9, 6], [43, 21, 15, 8]]

	print("\nArray:\n{}\n{}\n{}\n{}\n{}\n".format(arr[0], arr[1], arr[2], arr[3], arr[4]))
	print("\t--- AFTER ALGORITHM ---\n")
	res = part1_b(arr)
	print("\nArray:\n{}\n{}\n{}\n{}\n{}\n".format(res[0], res[1], res[2], res[3], res[4]))
	print("----------------------------------------\n")

	print("-------------- PART1_C TEST --------------")

	arr = [[37, 23, 24, 32], [21, 6, 7, 10], [53, 34, 30, 31], [32, 13, 9, 6], [43, 21, 15, 8]]

	print("\nArray:\n{}\n{}\n{}\n{}\n{}\n".format(arr[0], arr[1], arr[2], arr[3], arr[4]))
	print("\t--- AFTER ALGORITHM ---\n")
	res = part1_c(arr)
	print("\nArray:\n{}\n".format(res))
	print("----------------------------------------\n")

def driver2():
	print("-------------- PART2 TEST --------------")

	arr1 = list()
	n1 = random.randint(3,12)
	arr1.extend([random.randint(1,100) for i in range(n1)])
	arr1.sort()

	arr2 = list()
	n2 = random.randint(3,12)
	arr2.extend([random.randint(1,100) for i in range(n2)])
	arr2.sort()

	n = n1 + n2
	k = random.randint(1,n)

	print("\nArray1:\n{}\n".format(arr1))
	print("\nArray2:\n{}\n".format(arr2))
	print("\nk = {}\n".format(k))
	print("\t--- AFTER ALGORITHM ---\n")
	result = part2(arr1, arr2, k-1)
	print("{} th element: {}\n".format(k, result))
	print("----------------------------------------\n")

def driver3():
	print("-------------- PART3 TEST - 1 --------------")

	arr = [5, -6, 6, 7, -6, 7, -4, 3]
	print("\nArray:\n{}\n".format(arr))
	print("\t--- AFTER ALGORITHM ---\n")
	result = part3(arr)
	print("Largest Subset:\n{}\n".format(result))
	print("Sum: {}\n".format(sum(result)))
	print("----------------------------------------\n")

	print("-------------- PART3 TEST - 2 (RANDOM) --------------")

	arr = list()
	n = random.randint(4,12)
	arr.extend([random.randint(-100,100) for i in range(n)])
	print("\nArray:\n{}\n".format(arr))
	print("\t--- AFTER ALGORITHM ---\n")
	result = part3(arr)
	print("Largest Subset:\n{}\n".format(result))
	print("Sum: {}\n".format(sum(result)))
	print("----------------------------------------\n")

def driver4():
	print("-------------- PART4 TEST - 1 --------------")
	graph = [[0, 0, 0, 0, 0, 0, 0, 0],
			 [0, 1, 0, 1, 1, 0, 0, 1],
			 [1, 1, 1, 1, 0, 0, 0, 1],
			 [0, 1, 0, 1, 0, 1, 1, 0],
			 [1, 1, 0, 0, 1, 0, 0, 1],
			 [1, 0, 0, 1, 1, 1, 0, 1],
			 [1, 1, 1, 1, 1, 0, 1, 0],
			 [0, 1, 0, 0, 1, 0, 0, 1]]
	print("\nGraph:\n")
	print("[[0 0 0 0 0 0 0 0]\n [0 1 0 1 1 0 0 1]\n [1 1 1 1 0 0 0 1]\n [0 1 0 1 0 1 1 0]\n [1 1 0 0 1 0 0 1]\n [1 0 0 1 1 1 0 1]\n [1 1 1 1 1 0 1 0]\n [0 1 0 0 1 0 0 1]]")
	print("\t--- AFTER ALGORITHM ---\n")
	result = part4(graph)
	print("Yes\n") if result else print("No\n")
	print("----------------------------------------\n")

	print("-------------- PART4 TEST - 2 --------------")
	graph = [[0, 0, 0, 1, 0],
			 [0, 1, 0, 1, 0],
			 [1, 0, 0, 0, 1],
			 [0, 0, 1, 0, 1],
			 [0, 1, 1, 1, 0]]
	print("\nGraph:\n")
	print("[[0 0 0 1 0]\n [0 1 0 1 0]\n [1 0 0 0 1]\n [0 0 1 0 1]\n [0 1 1 1 0]]")
	print("\t--- AFTER ALGORITHM ---\n")
	result = part4(graph)
	print("Yes\n") if result else print("No\n")
	print("----------------------------------------\n")

	print("-------------- PART4 TEST - 3 --------------")
	graph = [[0, 0, 0, 0, 0],
			 [1, 1, 1, 0, 1],
			 [0, 1, 1, 1, 0],
			 [0, 0, 1, 1, 0],
			 [1, 0, 0, 1, 1]]
	print("\nGraph:\n")
	print("[[0 0 0 0 0]\n [1 1 1 0 1]\n [0 1 1 1 0]\n [0 0 1 1 0]\n [1 0 0 1 1]]")
	print("\t--- AFTER ALGORITHM ---\n")
	result = part4(graph)
	print("Yes\n") if result else print("No\n")
	print("----------------------------------------\n")


def driver5():
	print("-------------- PART5 TEST - 1 --------------")

	cost = [5, 11, 2, 21, 5, 7, 8, 12, 13, None]
	price = [None, 7, 9, 5, 21, 7, 13, 10, 14, 20]

	print("\nCost:\n{}\n".format(cost))
	print("\nPrice:\n{}\n".format(price))
	print("\t--- AFTER ALGORITHM ---\n")
	result = part5(cost, price)
	print("The best day to buy: {}\nGain: {}".format(result[2], result[1])) if result[0] else print("There is no day to make money!\n")
	print("----------------------------------------\n")

	print("-------------- PART5 TEST - 2 (RANDOM) --------------")

	n = random.randint(5,13)

	cost = list()
	cost.extend([random.randint(1,100) for i in range(n)])
	cost[-1] = None

	price = list()
	price.extend([random.randint(1,100) for i in range(n)])
	price[0] = None

	print("\nCost:\n{}\n".format(cost))
	print("\nPrice:\n{}\n".format(price))
	print("\t--- AFTER ALGORITHM ---\n")
	result = part5(cost, price)
	print("The best day to buy: {}\nGain: {}".format(result[2], result[1])) if result[0] else print("There is no day to make money!\n")
	print("----------------------------------------\n")

if __name__ == "__main__":

	print("\n!!! Every time the program runs, all test cases are randomly generated. !!!\n")

	driver1()
	driver2()
	driver3()
	driver4()
	driver5()

	print("\tAll tests finished.\n")
