def compute(node, ip, filename):
    print 'called compute function in compute_metrics.py'
    midstep = filename.split(".")
    newfilename= midstep[0] + "_filtered.txt"
    file = open(newfilename, "r")
    for line in file:
        node.append(line.split())
    file.close()
    computing(node, ip, midstep)
	
def computing(node, ip, midstep):
    reqsent = 0;
    reqrecieved = 0;
    repsent = 0;
    reprecieved = 0;
    for n1 in node:
        if n1[8] == "reply":
            if n1[2] == ip:
                repsent = repsent + 1
            elif n1[3] == ip:
                reprecieved = reprecieved + 1
        if n1[8] == "request":
            if n1[2] == ip:
                reqsent = reqsent + 1
            elif n1[3] == ip:
                reqrecieved = reqrecieved + 1

    output(reqsent, reqrecieved, repsent, reprecieved, node, ip, midstep)
    
def numRequestBytesSent(node, ip):
    total = 0
    for n1 in node:
        if n1[2] == ip and n1[8] == "request":
            total = total + int(n1[5])
    return total

def numRequestBytesRecieved(node, ip):
    total = 0
    for n1 in node:
        if n1[3] == ip and n1[8] == "request":
            total = total + int(n1[5])
    return total

def numRequestDataSent(node, ip):
    total = 0
    for n1 in node:
        if n1[2] == ip and n1[8] == "request":
            total = total + int(n1[5]) - 42
    return total

def numRequestDataRecieved(node, ip):
    total = 0
    for n1 in node:
        if n1[3] == ip and n1[8] == "request":
            total = total + int(n1[5]) - 42
    return total

# Logic for Time Metrics

def rtt(node, ip):
    total = 0
    count = 0
    for i in range(0, len(node), 2):
        if node[i][2] == ip and node[i][8] == "request":
            total = total + (float(node[i + 1][1]) - float(node[i][1]))
            count = count + 1
    return (total / count) * 1000

def echoRequestThroughput(node, ip):
    total = 0
    for i in range(0, len(node), 2):
        if node[i][2] == ip and node[i][8] == "request":
            total = total + (float(node[i + 1][1]) - float(node[i][1]))
    return (numRequestBytesSent(node, ip)/total)/1000

def echoRequestGoodput(node, ip):
    total = 0
    for i in range(0, len(node), 2):
        if node[i][2] == ip and node[i][8] == "request":
            total = total + (float(node[i + 1][1]) - float(node[i][1]))
    return (numRequestDataSent(node, ip)/total)/1000

def avgDelayReply(node, ip):
    total = 0
    h = 0
    for i in range(0, len(node), 2):
        if node[i][3] == ip and node[i][8] == "request":
            total = total + (float(node[i + 1][1]) - float(node[i][1]))
            h = h + 1
    return ((total/h) * 1000000)

def avgHop(node):
    hop = 0
    hopnum = 129
    requestcount = 0
    for i in range(0, len(node), 2):
        if node[i][8] == "request":
            hop = hop + (hopnum - (int("".join(filter(str.isdigit, node[i][11])))))
            requestcount = requestcount + 1

        else:
            continue
    return float(hop) / float(requestcount)

def output(reqsent, reqrecieved, repsent, reprecieved, node, ip, midstep):
    outputName = midstep[0]
    output = open("output.csv", "a")
    output.write(outputName)
    output.write("  \n")
    output.write("Echo Requests Sent" + "," + "Echo Requests Recieved" + "," + "Echo Replies Sent" + "," + "Echo Replies Recieved\n" )
    output.write(str(reqsent/2) + "," + str(reqrecieved/2) + "," + str(repsent/2) + "," + str(reprecieved/2) + "\n")
    output.write("Echo Request Bytes sent (bytes)" + "," + "Echo Request Data Sent (bytes)\n")
    output.write(str(numRequestBytesSent(node, ip)/2) + "," + str(numRequestDataSent(node, ip)/2) + "\n")
    output.write("Echo Request Bytes Recieved (bytes)" + "," + "Echo Request Data Recieved (bytes)\n")
    output.write(str(numRequestBytesRecieved(node, ip)/2) + "," + str(numRequestDataRecieved(node, ip)/2) + "\n")
    output.write(" \n")

    output.write("Average RTT (miliseconds)" + "," + str(rtt(node, ip)) + "\n")
    output.write("Echo Request Throughput (kB/sec)" + "," + str(echoRequestThroughput(node, ip)) + "\n")
    output.write("Echo Request Goodput (kB/sec)" + "," + str(echoRequestGoodput(node, ip)) + "\n")
    output.write("Average Reply Delay" + "," + str(avgDelayReply(node, ip)) + "\n")
    output.write("Average Echo Request Hop Count" + "," + str(avgHop(node)) + "\n")
    output.write(" \n")

    


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


	
