def compute(L) :
	print 'called compute function in compute_metrics.py'
	computing(L)
	
def computing(L):
	reqsent = 0;
	reqrecieved = 0;
	
	repsent = 0;
	reprecieved = 0;
	
	for i in range(len(L)):
		print L[i][10]
	
		if L[i][8] == "reply":
			if L[i][2] == "192.168.100.1":
				repsent = repsent + 1
			elif L[i][3] == "192.168.100.1":
				reprecieved = reprecieved + 1
				
		if L[i][8] == "request":
			if L[i][2] == "192.168.100.1":
				reqsent = reqsent + 1
			elif L[i][3] == "192.168.100.1":
				reqrecieved = reqrecieved + 1
				
	
	print "Requests Sent: " + str(reqsent)
	print "Requests Recieved: " + str(reqrecieved)
	
	print "Replies Sent: " + str(repsent)
	print "Replies Recieved: " + str(reprecieved)
	
	
			

		
# Node 1 - 192.168.100.1
# Node 2 - 192.168.100.2
# Node 3 - 192.168.200.1
# Node 4 - 192.168.200.2
# Node 5 - 192.168.100.254
		
	
	
# 0 - Number
# 1 - Time
# 2 - Src IP
# 3 - Dest IP
# 4 - ICMP
# 5 - Length
# 6 - Echo                | Destination
# 7 - Ping                | Unreachable
# 8 - reply/request       | (Host
# 9 - ID                  | Unreachable)
#10 - SEQ
#11 - TTL
#12 - (reply/request
#13 - in
#14 - Reply Time


	
