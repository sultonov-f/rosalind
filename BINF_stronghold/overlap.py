import sys
def getFasta(path):
        dic={}
        with open(path,"r") as file:
                fasta = file.read();
        reads = fasta.split(">")
        for read in  reads:
                if read:
                        dic[read.split("\n")[0]]="".join(read.split("\n")[1:])
                                                        #[len(l) for l in>
        #123
        return dic
if __name__=="__main__":
        if len(sys.argv)==2:
                res= getFasta(sys.argv[1])
                print (res) 
