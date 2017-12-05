import hmac
from hashlib import sha1
import time as t
import base64
import struct

digit = 6
time_inc = 30
key = "abcd efgh ijkl mnop"
key = key.upper()
key = key.replace(" ", "") 

print key
counter = 0

while 1==1:
        if((t.time())% time_inc == 0):
                # Every 30 seconds
                counter = int(t.time()/time_inc)
                counter = struct.pack('>Q', counter)  # Used from GitHub User acoster, https://gist.github.com/acoster/4121786
                hash_new = hmac.new(base64.b32decode(key), str(counter), sha1)
                s = hash_new.hexdigest()
                #Find lower 4 bits of byte 19
                index = int(s[39], 16) * 2
                #Index to that byte to that byte + 3
                string = s[index:index+8]
                #Mask out highest bit
                string = bin(int(string, 16))
                string = string[2:].zfill(32)
                string = string[1:]  #Just chop the first bit

                #Modulo with 10^digit
                totp = int(string, 2) % (10**digit)
                print str(totp).zfill(6)



