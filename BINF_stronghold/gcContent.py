import sys
def countGC(dna):
	tempDNA = dna.upper()
	gc=0
	gc_percentage = 0.00
	for bp in tempDNA:
		if bp in "GC":
			gc+=1
	gc_percentage = (gc / len(tempDNA)) * 100
	return gc,gc_percentage
def getGC(path):
	dic={}
	with open(path,"r") as file:
		fasta = file.read();
	reads = fasta.split(">")
	for read in  reads:
		if read:
			dic[read.split("\n")[0]]="".join(read.split("\n")[1:])
							#[len(l) for l in read.split("\n")[1:]]
	total_size={k: countGC(v) for k,v in dic.items() if len(v) > 1}
	return total_size
if __name__=="__main__":
	if len(sys.argv)==2:
		res= getGC(sys.argv[1])
		max_key = max(res.items(), key=lambda item: item[1][1])
		print (max_key[0],max_key[1][1]) 
