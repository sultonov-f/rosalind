def countRab(n,k):
	tempArr=[0,1]
	for i in range(2, n+1):
		tempArr.append(tempArr[i-1]+(tempArr[i-2]*k))
	return tempArr
if __name__=="__main__":
	months=36
	pairs=4
	res = countRab(months,pairs)
	print(res[months])
