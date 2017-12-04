import hmac
from hashlib import sha1
import time as t

digit = 6
time_inc = 5
key = "abcdefghijklmnop"
print key
counter = 0

t0 = 0 #So the first one runs, then times to the second
while 1==1:
        if(t0 == 0 or (t0-t.time())% time_inc == 0):
                # Every 30 seconds
                t0 = t.time()
                hash_new = hmac.new(key, str(counter), sha1)
                s = hash_new.hexdigest()
                #Find lower 4 bits of byte 19
                index = int(s[39], 16)
                #Index to that byte to that byte + 3
                string = s[index:index+8]
                #Mask out highest bit
                string = bin(int(string, 16))
                string = string[2:].zfill(32)
                string = string[1:]  #Just chop the first bit

                #Modulo with 10^digit
                totp = int(string, 2) % (10**digit)
                print totp
                counter += 1



