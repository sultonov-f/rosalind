def compl(dna):
	tempDNA=dna[::-1].upper()
	result=""
	for bp in tempDNA:
		match bp:
			case "A":
				result+="T"
			case "C":
				result+="G"
			case "G":
				result+="C"
			case "T":
				result+="A"
	return result
if __name__=="__main__":
	dna=input("DNA:")
	print("\ncomplementation:\n",compl(dna))
