from filter_packets import *
from packet_parser import *
from compute_metrics import *

import sys

fileName = sys.argv[1]

filter(fileName)
parse(fileName)
compute()


