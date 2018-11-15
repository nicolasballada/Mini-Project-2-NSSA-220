import sys

def filter(fn) :
    fileName = sys.argv[1]
    read( fileName )
	
def read(fn) :
    file = open(fn, 'r')
    for line in file :
        if 'ICMP' in line :
        print("got it")
    file.close()
	
	
	
	
	
