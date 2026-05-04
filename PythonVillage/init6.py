import sys

def countText(text):
	dic={}
	for word in text:
		dic[word] = dic.get(word, 0) + 1
	return dic

def getText(path):
	res=""
	with open(path,"r") as file:
		text = file.read();
	text=text.replace("\n","")
	temp = text.split(" ")
	return temp
if __name__=="__main__":
	if len(sys.argv)==2:
		res= getText(sys.argv[1])
		result = countText(res)
		print(''.join([str(k)+" "+str(i)+"\n" for k,i in result.items()]))
