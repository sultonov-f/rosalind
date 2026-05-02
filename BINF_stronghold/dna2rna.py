def dna2rna(dna):
	tempDNA= dna.upper()
	result=""
	for bp in tempDNA:
		if bp=="T":
			result+="U"
		else:
			result+=bp
	return result
if __name__=="__main__":
	dna=input("DNA:")
	print("\nRNA:\n"dna2rna(dna))
