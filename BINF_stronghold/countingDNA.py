def countDNA(dna):
	tempDNA = dna.upper()
	dic={"A":0,"C":0,"G":0,"T":0}
	for bp in tempDNA:
		dic[bp]+=1
	return dic
if __name__=="__main__":
	dna=input()
	result =countDNA(dna)
	print(' '.join([str(i) for k,i in result.items()]))

