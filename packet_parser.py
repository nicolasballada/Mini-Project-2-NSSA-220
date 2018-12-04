def parse(fn) :
	print 'called parse function in packet_parser.py'
	parsedata(fn)
	
def parsedata(file_name):
	mid_step = file_name.split(".")
	new_file_name = mid_step[0] + "_filtered." + mid_step[1]
	filtered_node = open(new_file_name, "r")
	
	line = filtered_node.readline()
    
	
	
	while line:
		if "request" in line:
			
		if "reply" in line:
			

		line = filtered_node.readline()
	
packet = []
L = []



