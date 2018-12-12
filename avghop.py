def avgHop(node):
    hop = 0
    hopnum = 129
    requestcount = 0
    for i in range(0, len(node), 2):
        if node[i][8] == "request":
            hop = hop + (hopnum - (int(filter(str.isdigit, node[i][11]))))
            requestcount = requestcount + 1

        else:
            continue
    return float(hop) / float(requestcount)
