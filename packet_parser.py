def parse(fn, L) :
	print 'called parse function in packet_parser.py'
	parsedata(fn, L)
	
def parsedata(file_name, L):
	mid_step = file_name.split(".")
	new_file_name = mid_step[0] + "_filtered." + mid_step[1]
	filtered_node = open(new_file_name, "r")
	
	line = filtered_node.readline()
    
	while line:
		L.append(line.strip().split())
		line = filtered_node.readline()
		
	filtered_node.close()
	



