def countMutation(read1, read2):
	result=0
	for bp in range(len(read1)):
		if read1[bp] != read2[bp]:
			result+=1
	return result

if __name__=="__main__":
	read1= input("read1:")
	read2= input ("\nread2:")
	dif = countMutation(read1,read2)
	print("\n\n",dif)
