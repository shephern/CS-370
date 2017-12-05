Nathan Shepherd
CS 370 - Assigment #3

Running Instructions:

This code is run by the ./submission command. 
It will require that you chmod it properly, or use sh ./submission.

Python Explanation:

I was unable to find the library that you mentioned would speed the project,
but regardless I feel like I understand TOTP well enough to explain.
TOTP stands for time-based one time password, and is implemented as a hmac 
based one-time password, HOTP, with the counter being the number of time 
steps since the UNIX epoch.
The initial step of the program is to get a password from the user.
This password is the key used to encrypt the counter, which in TOTP is the 
time steps.
For this implementation the counter is unix  t0/30, as a new password is 
given every 30 seconds.
Once the password and time steps have been collected the program then the
program hashes the counter with the key, using sha1 with hmac.
This ensures that, without the key, it is infeasible to derive the hash.
Once hashed the hash must be simplified for the users.
This is done by indexing to a portion of the hash, and modulusing the part
to a desired length.
The indexing is chosen by the lowest bit of the last byte in the hash,
and three bytes following.
With these four bytes the highest byte is masked out, because of the 
confusion it might cause with signed and unsigned processors.
Once it is masked, then all the program requires is to modulus the 4 byte
number with 10^6, for a 6 digit number.

In this project I used the RFC documents 6238 and 4226.
I also got the idea to use struct.pack() from acoster and https://gist.github.com/acoster/4121786.
Further information came from Robbiev at https://garbagecollected.org/2014/09/14/how-google-authenticator-works/
