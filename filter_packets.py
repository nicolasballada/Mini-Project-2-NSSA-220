import sys

def filter( fileName ) :
    read( fileName )
	
def read(fn) :
    file = open(fn, 'r')
    for line in file :
        if 'ICMP' in line :
        print("got it")
    file.close()
	
	
	
	
	
