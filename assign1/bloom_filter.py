#!/bin/python
import sys
import pyhash
import math
import time as t
##############################
## Assignment 1- CS 370
## Nathan Shepherd
## Bloom Filter
## Using the Pyhash Library
## --From GitHub user: flier
##############################

dict_name = ""
input_name = ""
out_name1 = ""
out_name2 = ""

#Declasre hash functions, 
hash1 = pyhash.city_64()
hash2 = pyhash.spooky_64()
hash3 = pyhash.metro_64()
hash4 = pyhash.mum_64()
hash5 = pyhash.xx_64()

for i in range(0, len(sys.argv)):
        if (sys.argv[i] == '-d' and len(sys.argv) > i+1):
                dict_name = sys.argv[i+1]
        elif (sys.argv[i] == '-i' and len(sys.argv) > i+1):
                input_name = sys.argv[i+1]
        elif (sys.argv[i] == '-o' and len(sys.argv) > i+2):
                out_name1 = sys.argv[i+1]
                out_name2 = sys.argv[i+2]

if (dict_name == "" or input_name == "" or out_name1 == "" or out_name2 == ""):
        print("USAGE: bloom_filter.py -d dictionary -i input -o output1 output2")

dictionary = open(dict_name, "r")
input_file = open(input_name, "r")
out1 = open(out_name1, "w")
out2 = open(out_name2, "w")
#Create two bloom filters(One 3 hash fxns, one 5 hash fxns)
#Bit Length
input_size = sum(1 for line in dictionary) + sum(1 for line in input_file)

#Optimize array size based off k and input size
#I tried using optimized values, but it had to high prob of false positives
# over 12%
# so I graphed the (1-e^-kn/m)^k with m as the independent, and minimized that
# I decided on 7.5 mil because it got to 1% which is more acceptable
m1 = 7500000 #int(round(input_size*(3/math.log(2))))  
m2 = 7500000 #int(round(input_size*(5/math.log(2))))

#Run Dictionary through both of them
bloom_filter1 = [0]*m1
bloom_filter2 = [0]*m2

dictionary.seek(0)  # Jump to beginning of file
input_file.seek(0)
for bad_pass in dictionary:
        bit1 = int(hash1(bad_pass))
        bit2 = int(hash2(bad_pass))
        bit3 = int(hash3(bad_pass))
        bit4 = int(hash4(bad_pass))
        bit5 = int(hash5(bad_pass))

        # Set the first bloom filters bits
        bloom_filter1[bit1%m1] = bloom_filter1[bit2%m1] = \
                bloom_filter1[bit3%m1] = 1
        # Set the second bloom filter bits
        bloom_filter2[bit1%m2] = bloom_filter2[bit2%m2] = \
                bloom_filter2[bit3%m2] = bloom_filter2[bit4%m2] = \
                bloom_filter2[bit5%m2] = 1

#time_tot3 = 0
#time_tot5 = 0
#Run each potential password through both
for test_password in input_file:
        #time3 = time5 = t.time()
        bit1 = int(hash1(test_password))
        bit2 = int(hash2(test_password))
        bit3 = int(hash3(test_password))
        #time3 = t.time() - time3
        bit4 = int(hash4(test_password))
        bit5 = int(hash5(test_password))
        #time5 = t.time() - time5
        
        #time_check = t.time()
        in1 = bloom_filter1[bit1%m1] + bloom_filter1[bit2%m1] + \
                bloom_filter1[bit3%m1]
        
        #Produce two files, for each bloom
        if in1 == 3:
                out1.write("maybe\n")
        else:
                out1.write("no\n")
        
        #time_check = t.time() - time_check
        #time3 += time_check
        #time_tot3 += time3
        #time_check = t.time()
        in2 = bloom_filter2[bit1%m2] + bloom_filter2[bit2%m2] + \
                bloom_filter2[bit3%m2] + bloom_filter2[bit4%m2] + \
                bloom_filter2[bit5%m2]
        if in2 == 5:
                out2.write("maybe\n")
        else:
                out2.write("no\n")
        #time_check = t.time() - time_check
        #time5 += time_check

        #time_tot5 += time5



#print "Using 3 hash functions took:",time_tot3*1000,"msecs\n"
#print "Using 5 hash functions took:",time_tot5*1000,"msecs\n"
# Close all files
input_file.close()
dictionary.close()
out1.close()
out2.close()

