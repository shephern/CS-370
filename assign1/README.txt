Nathan Shepherd
README.txt
Program 1: Bloom Filter

TO RUN:
run with python 2.7.5

Dependencies:
math, sys // Already in python
pyhash
        : Install with 'pip install --user pyhash'

run with 'make' or python bloom_filter.py -d dictionary.txt -i input.txt 
                        -o out1.txt out2.txt

clean with 'make clean'

1:  I chose non-crypto hash functions, as they were faster.  I went with 64
bit, because that was beyond my bit array size, and so I could use mod to 
index to the array.  This gave me a output width of 64 bit, with 2^64 random
integers, as the hashses, to my knowledge are unsigned.The hash library I 
used was pyhash, by GitHub user flier.  In each case, both k=3 and k=5 I
used a size of 7.5 million, as at that point both approximately had a 
collision chance of 1%.  I had initially used k = (m/n)ln(2) to approximate
the array size, but that gave me a collision chance of 12%, and I wanted 
more.

2:  Using the sample_input.txt I averaged the time that each password took.
With the three hash functions the checking took, on average, .0327 
milleseconds.  With five hash funcitons it took .0337 msec.  This difference
is small but it does make sense.  In this algorithm the longest chunk of 
time is taken by the hashing, and if each hashing can do it at a certain
rate, it would follow that two additional hashes would take longer.  A 
reason that this is not a proportional time difference could be that not
all hash functions are equally fast, and the timing included indexing which
could take a significant amount of time as well.

3:  As mentioned in part 1, the probability of collision for both of my 
bloom filters is 1%.  To be exact:

bloom w/ 3: (1-e^-3(623517)/7.5e6)^3 = .0107 or 1%
bloom w/ 5: (1-e^-5(623517)/7.5e6)^5 = .0046 or 0.5%

The probability of a false negative is 0%, as a bloom filter is based off
deterministic hash functions that will index the same location for the same
password input. This means that if a password is put in, then checked, the
indexed bits will always be set.

4:  To reduce the rate of False Positives I increased the array size. 
You could concievably, with a set input size, increase the array size to
the point that there are no false positives, but 1% was satisfatory to me
for this project.


