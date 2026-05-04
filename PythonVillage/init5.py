import sys

def getText(path):
	res=""
	with open(path,"r") as file:
		text = file.read();
	temp = text.split("\n")
	res=res.join([str(temp[i])+"\n" for i in range(len(temp)) if (i % 2) == 1])
	return res
if __name__=="__main__":
	if len(sys.argv)==2:
		res= getText(sys.argv[1])
		print (res)
