'''
QUEEN'S UNIVERSITY
CISC 235 2015W
Assignment 3
Brianna Rubin
'''

import math

#variables for table sizes (M), values for c1 and c2, and initiating Tables
M1 = 4695
M2 = 2053
T1 = []
T2 = []
c1s = [1,0.5,2]
c2s = [1,0.5,2]

#initiating lists for probe sequence lengths
quad_seq_lengths = []
doub_seq_lengths = []

#File I/O to import keys to be inserted, and add them to a list
names = []
file = open("secret_data.txt",'r')
for line in file:
    names.append(line)

#function that converts a string to an integer value based on
#ascii codes

def hash1(key):
    sum = 0
    for i in range(len(key)):
        sum = sum*17 + ord(key[i])
    return sum

#The 3 hash functions used to test double hashing

def hash2(key):
    plus = key + 3
    return int(plus%M2)

def hash3(key):

    m = 0.5*(math.sqrt(5)) - 1
    A = 5
    s = key*A
    x = 0.9*s
    return int(math.ceil(m*x))

def hash4(key):
    return (key**32)%M2

def Quadratic_Probing_Insert(c1, c2, M, T, k):
    seq = 1
    i = 0
    v = hash1(k) % M
    a = v
    while (i < M) and (T[int(a)] != "")  and (T[int(a)] != "deleted"):
        seq += 1
        i += 1
        a = (v + c1*i + c2*(i**2)) % M
    quad_seq_lengths.append(seq)
    if (T[int(a)] is "") or (T[int(a)] is "deleted"):
        T[int(a)] = k
    else:
        print "table full, insert failed"

def Double_Hashing_Insert(x, M, T, k):
    seq = 1
    i = 0
    v = hash1(k) % M
    a = v

    while (i < M2) and (T[int(a)] != "")  and (T[int(a)] != "deleted"):
        seq += 1
        i += 1
        if x == 0:
            a = (hash2(v) + i*hash3(v)) % M
        elif x == 1:
            a = (hash2(v) + i*hash4(v)) % M
        else:
            a = (hash3(v) + i*hash4(v)) % M
    doub_seq_lengths.append(seq)
    if (T[int(a)] is "") or (T[int(a)] is "deleted"):
            T[int(a)] = k
    else:
        #print k
        print "table full, insert failed"

def main():
    for x in range(3):
        c1 = c1s[x]
        c2 = c2s[x]
        print "c1 = ",c1, " c2 = ",c2
        print "Quadtratic Probing:"
        T1 = []
        for i in range (M1):
            T1.append("")


        for i in range(len(names)):
            Quadratic_Probing_Insert(c1, c2, M1,T1,names[i])

        quad_sum = 0
        for j in quad_seq_lengths:
            quad_sum += j

        quad_ave_length = quad_sum/float(len(quad_seq_lengths))


        print "Average probe sequence length: ",quad_ave_length
        print "Double Hashing:"
        T2 = []

        for i in range (M2):
            T2.append("")

        for i in range(len(names)):
            Double_Hashing_Insert(x, M2,T2,names[i])

        doub_sum = 0
        for j in doub_seq_lengths:
            doub_sum += j

        doub_ave_length = doub_sum/float(len(doub_seq_lengths))

        print "Average probe sequence length: ",doub_ave_length


main()
