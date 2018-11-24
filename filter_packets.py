#!/bin/python

import sys

def filter(fn):
    read(fn)

def read(file_name):
    mid_step = file_name.split(".")
    new_file_name = mid_step[0] + "_filtered." + mid_step[1]

    unfiltered_node = open(file_name, "r")
    filtered_node = open(new_file_name, "a")

    line = unfiltered_node.readline()

    while line:
        if "ICMP" in line:
            filtered_node.write(line)
            line = unfiltered_node.readline()
            filtered_node.write(line)
        line = unfiltered_node.readline()


fn = "file.txt"

init(fn)

	
	
	
