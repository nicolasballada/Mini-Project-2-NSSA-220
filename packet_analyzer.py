from filter_packets import *
from packet_parser import *
from compute_metrics import *

import sys

fileName = sys.argv[1]

L = []

filter(fileName)
parse(fileName, L)
compute(L)



