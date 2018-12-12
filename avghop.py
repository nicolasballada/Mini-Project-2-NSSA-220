def avgHop(node):
	hop = 0
	hopnum = 129
	requestcount = 0
	for i in range(0, len(node), 2):
		if node[8] == "request":
			hop = hopnum - (hop + int("".join(filter(str.isdigit, hop[11]))))
			requestcount = requestcount + 1
			
		else:
			continue
	return float(hop)/float(requestcount)