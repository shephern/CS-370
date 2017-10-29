#!/bin/python
import sys

##############################
## Assignment 1- CS 370
## Nathan Shepherd
## Bloom Filter
##############################

dict_name = ""
input_name = ""
out_name1 = ""
out_name2 = ""

for i in range(0, len(sys.argv)):
        if (sys.argv[i] == '-d' and len(sys.argv) > i+1):
                dict_name = sys.argv[i+1]
        elif (sys.argv[i] == '-i' and len(sys.argv) > i+1):
                input_name = sys.argv[i+1]
        elif (sys.argv[i] == '-o' and len(sys.argv) > i+2):
                out_name1 = sys.argv[i+1]
                out_name2 = sys.argv[i+2]

print(dict_name + input_name + out_name1 + out_name2)
