import random
import numpy as np 

def part1 (NY, SF, M) :

	length = len(NY)
	optNY = [0 for i in range(length+1)]
	optSF = [0 for i in range(length+1)]
	

	for i in range(1, length + 1):
		optNY[i] = NY[i-1] + min(optNY[i-1], (M + optSF[i-1]))
		optSF[i] = SF[i-1] + min(optSF[i-1], (M + optNY[i-1]))

	return min(optNY[length], optSF[length])

def part2 (begins, lengths):

	finishes = list()
	indexlist = list()
	for i in range(len(lengths)):
		finishes.append(begins[i] + lengths[i])

	sortedfinish = finishes.copy()
	sortedfinish.sort()
	sortedbegins = list()
	for i in sortedfinish:
		index = finishes.index(i)
		sortedbegins.append(begins[index])
		indexlist.append(index)
		finishes[index] = -1
		begins[index] = -1

	return part2_helper(sortedbegins, sortedfinish, indexlist)

def part2_helper (starts, finishes, indexlist): 

	session = list()
	n = len(finishes) 
	i = 0
	session.append(indexlist[i])
	for j in range(n): 
		if starts[j] >= finishes[i]: 
			session.append(indexlist[j])
			i = j

	return session

import numpy as np 

def part3(arr):

	dp = np.zeros((51, 1000)) 
	visit = np.zeros((51, 1000))
	res = part3_helper(0, 0, arr, list(), len(arr), dp, visit)
	if(res != 1):
		print("Subset with total sum of elements equal to zero:")
		print(res)
		print("")
	else:
		res = None
		print("There is no subset with total sum of elements equal to zero.\n")
	return res

def part3_helper(i, s, arr, arr2, n, dp, visit) : 

	if (i == n) : 
		if (s == 0) :
			if(len(arr2) != 0):
				return arr2
			return 1  
		else : 
			return 0

	arrSize = 51 
	if (visit[i][s + arrSize]) : 
		return dp[i][s + arrSize] 

	visit[i][s + arrSize] = 1  
	arr3 = arr2.copy()
	arr3.append(arr[i])

	temp = part3_helper(i + 1, s + arr[i], arr, arr3.copy(), n, dp, visit)
	if(temp != 0 and temp != 1):
		return temp

	temp2 = part3_helper(i + 1, s, arr, arr2.copy(), n, dp, visit)
	if(temp2 != 0 and temp2 != 1):
		return temp2

	dp[i][s + arrSize ] = temp + temp2

	return dp[i][s + arrSize] 

def part4(str1, str2, match = 2, mismatch = -2, gap = -1):

	len1 = len(str1)
	len2 = len(str2)

	D = [[0 for x in range(len1 + len2 + 1)] for y in range(len1 + len2 + 1)]

	for i in range(len1 + len2 + 1):
		D[i][0] = gap * i
		D[0][i] = gap * i

	for i in range(1, len1 + 1):
		for j in range(1, len2 + 1):
			if str1[i-1] == str2[j-1]:
				D[i][j] = D[i-1][j-1] + match
			else:
				D[i][j] = max((D[i - 1][j - 1] + mismatch), (D[i - 1][j] + gap), (D[i][j - 1] + gap));

	i = len1
	j = len2
	l = len1 + len2

	xpos = l
	ypos = l

	xans = [0 for x in range(l+1)]
	yans = [0 for x in range(l+1)]

	while not (i==0 or j==0):
		if str1[i-1] == str2[j-1]:
			xans[xpos] = str1[i - 1]
			yans[ypos] = str2[j - 1]
			i -= 1
			j -= 1
			xpos -= 1
			ypos -= 1
		elif (D[i-1][j-1] + mismatch) == D[i][j]:
			xans[xpos] = str1[i - 1] 
			yans[ypos] = str2[j - 1]
			i -= 1
			j -= 1
			xpos -= 1
			ypos -= 1
		elif (D[i-1][j] + gap) == D[i][j]:
			xans[xpos] = str1[i - 1]
			yans[ypos] = "_"
			i -= 1
			xpos -= 1
			ypos -= 1
		elif (D[i][j-1] + gap) == D[i][j]:
			xans[xpos] = "_"
			yans[ypos] = str2[j - 1]
			j -= 1
			xpos -= 1
			ypos -= 1

	while (xpos > 0):
		if (i > 0):
			i -= 1
			xans[xpos] = str1[i]
			xpos -= 1
		else:
			xans[xpos] = "_"
			xpos -= 1

	while (ypos > 0):
		if (j > 0):
			j -= 1
			yans[ypos] = str2[j]
			ypos -= 1
		else:
			yans[ypos] = "_"
			ypos -= 1

	i = l
	while i >= 1:
		if(yans[i] == "_" and xans[i] == "_"):
			id = i + 1
			break
		i -= 1
	i += 1

	res1 = "".join(xans[i:])
	res2 = "".join(yans[i:])

	return (D[len1][len2], res1, res2)

def part5 (arr):

	opCount = 0

	while (len(arr) > 1):
		x = min(arr)
		arr.remove(x)
		y = min(arr)
		arr.remove(y)
		arr.append(x+y)
		opCount += (x+y)

	return(arr[0], opCount)

def driver1():
	print("-------------- PART1 TEST --------------")

	n = 4
	NY = [1, 3, 20, 30]
	SF = [50, 20, 2, 4]

	M = 10

	print("\n Move Cost = {}".format(M))
	print("\n#",end="")
	for i in range(n):
		print("\tM-{}".format(i+1), end="")
	print("")

	print("NY\t",end="")
	for i in range(n) :
		print("{}\t".format(NY[i]), end="")
	print("")

	print("SF\t",end="")
	for i in range(n) :
		print("{}\t".format(SF[i]), end="")

	print("\n\n\t--- AFTER ALGORITHM ---\n")
	result = part1(NY, SF, M)
	print("Total cost:\n{}\n".format(result))
	print("----------------------------------------\n")

	print("--------- PART1 TEST (RANDOM) ----------")

	n = random.randint(3,8)
	NY = list()
	NY.extend([random.randint(1,100) for i in range(n)])

	SF = list()
	SF.extend([random.randint(1,100) for i in range(n)])

	M = random.randint(5,25)

	print("\n Move Cost = {}".format(M))
	print("\n#",end="")
	for i in range(n):
		print("\tM-{}".format(i+1), end="")
	print("")

	print("NY\t",end="")
	for i in range(n) :
		print("{}\t".format(NY[i]), end="")
	print("")

	print("SF\t",end="")
	for i in range(n) :
		print("{}\t".format(SF[i]), end="")

	print("\n\n\t--- AFTER ALGORITHM ---\n")
	result = part1(NY, SF, M)
	print("Total cost:\n{}\n".format(result))
	print("----------------------------------------\n")

def driver2():

	print("-------------- PART2 TEST --------------")

	n = 7
	starts = [7, 12, 6, 8, 11, 3, 11]
	lengths = [10, 10, 7, 1, 10, 5, 11]

	print("\nSession start time list:\n{}\n".format(starts))
	print("\nSession length list:\n{}\n".format(lengths))
	print("After random generated start and length list:")
	finishes = [starts[i] + lengths[i] for i in range(n)]
	print("\nSession finish list:\n{}\n".format(finishes))
	print("\t--- AFTER ALGORITHM ---\n")
	result = part2(starts.copy(), lengths.copy())
	print("List of indexes of optimal sessions: {}\n".format(result))
	print("Maximum number of sessions: {}\n".format(len(result)))
	print("Optimal Sessions: (start, length, finish) \n")
	j = 1
	for i in result:
		print("{}- \t\t\t({}, {}, {})\n".format(j, starts[i], lengths[i], starts[i]+lengths[i]))
		j += 1
	print("----------------------------------------\n")

	print("--------- PART2 TEST (RANDOM) ----------")

	starts = list()
	n = random.randint(4,10)
	starts.extend([random.randint(1,12) for i in range(n)])

	lengths = list()
	lengths.extend([random.randint(1,12) for i in range(n)])

	print("\nSession start time list:\n{}\n".format(starts))
	print("\nSession length list:\n{}\n".format(lengths))
	print("After random generated start and length list:")
	finishes = [starts[i] + lengths[i] for i in range(n)]
	print("\nSession finish list:\n{}\n".format(finishes))
	print("\t--- AFTER ALGORITHM ---\n")
	result = part2(starts.copy(), lengths.copy())
	print("List of indexes of optimal sessions: {}\n".format(result))
	print("Maximum number of sessions: {}\n".format(len(result)))
	print("Optimal Sessions: (start, length, finish) \n")
	j = 1
	for i in result:
		print("{}- \t\t\t({}, {}, {})\n".format(j, starts[i], lengths[i], starts[i]+lengths[i]))
		j += 1
	print("----------------------------------------\n")

def driver3():
	print("------------ PART3 TEST - 1 ------------")

	arr = [-1, 6, 4, 2, 3, -7, -5]
	print("\nArray:\n{}\n".format(arr))
	print("\t--- AFTER ALGORITHM ---\n")
	result = part3(arr)
	print("----------------------------------------\n")

	print("------------ PART3 TEST - 2 ------------")

	arr = [-18, 7, 12, 13, 4, 3, 13, 16, 5]
	print("\nArray:\n{}\n".format(arr))
	print("\t--- AFTER ALGORITHM ---\n")
	result = part3(arr)
	print("----------------------------------------\n")

def driver4():
	print("------------ PART4 TEST - 1 ------------")

	str1 = "alignment"
	str2 = "slime"
	match = 2
	mismatch = -2
	gap = -1
	print("\nSequence A: {}".format(str1))
	print("\nSequence B: {}".format(str2))
	print("\nmatch_score = {},\tmismatch_score = {},\tgap_score = {}\n". format(match, mismatch, gap))
	print("\t--- AFTER ALGORITHM ---\n")
	result = part4(str1, str2, match, mismatch, gap)
	print("\nAlignment of sequence A: {}".format(result[1]))
	print("\nAlignment of sequence B: {}".format(result[2]))
	print("\nCost: {}".format(result[0]))
	print("----------------------------------------\n")

	print("------------ PART4 TEST - 2 ------------")

	str1 = "homework"
	str2 = "coworker"
	match = 3
	mismatch = -3
	gap = -2
	print("\nSequence A: {}".format(str1))
	print("\nSequence B: {}".format(str2))
	print("\nmatch_score = {},\tmismatch_score = {},\tgap_score = {}\n". format(match, mismatch, gap))
	print("\t--- AFTER ALGORITHM ---\n")
	result = part4(str1, str2, match, mismatch, gap)
	print("\nAlignment of sequence A: {}".format(result[1]))
	print("\nAlignment of sequence B: {}".format(result[2]))
	print("\nCost: {}".format(result[0]))
	print("----------------------------------------\n")

def driver5():
	print("-------------- PART5 TEST --------------")

	arr = [11,12,1,7,10]
	print("\nArray:\n{}\n".format(arr))
	print("\t--- AFTER ALGORITHM ---\n")
	result = part5(arr)
	print("Sum of elements: {}\nMinimum number of operations: {}\n".format(result[0], result[1]))
	print("----------------------------------------\n")

	print("--------- PART5 TEST (RANDOM) ----------")

	arr = list()
	n = random.randint(3,10)
	arr.extend([random.randint(1,100) for i in range(n)])
	print("\nArray:\n{}\n".format(arr))
	print("\t--- AFTER ALGORITHM ---\n")
	result = part5(arr)
	print("Sum of elements: {}\nMinimum number of operations: {}\n".format(result[0], result[1]))
	print("----------------------------------------\n")

if __name__ == "__main__":

	print("\n!!! Every time the program runs, some test cases are randomly generated. Some test cases are hard coded. !!!\n")

	driver1()
	driver2()
	driver3()
	driver4()
	driver5()

	print("\tAll tests finished.\n")