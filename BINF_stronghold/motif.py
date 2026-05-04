def findMotif(dna,motif):
	pos=[]
	result=[]
	tempDNA = dna.upper()
	for bpi in range(len(tempDNA)):
		if tempDNA[bpi] == motif.upper()[0]:
			pos.append(bpi)
	for pm in pos:
		if tempDNA[pm:pm+len(motif)]==motif.upper():
			result.append(pm+1)
	return result
if __name__=="__main__":
	dna=input("DNA:")
	motif=input("MOTIF:")
	res=findMotif(dna,motif)
	print(*res)
