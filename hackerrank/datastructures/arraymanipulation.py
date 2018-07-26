import math
import os
import random
import re
import sys
import numpy as np

def arrayManipulation(n, queries):
    array = [0 for i in range(n)]
    currentInt = 0
    maxInt = 0
    for start,end,addAmount in queries:
        array[start-1] += addAmount
        array[end] -= addAmount
    for el in array:
        currentInt += el
        if currentInt>maxInt:
            maxInt = currentInt
    return maxInt

def nparrayManipulation(n, queries):
    array = np.zeros((n,))
    currentInt = 0
    maxInt = 0
    for start,end,addAmount in queries:
        array[start-1] += addAmount
        array[end] -= addAmount
    for el in array:
        currentInt += el
        if currentInt>maxInt:
            maxInt = currentInt
    return maxInt
    

if __name__ == '__main__':
    data = open(r'C:\Users\Karlm\Documents\AlgorithmSkills\hackerrank\datastructures\arraymanipulationdata', 'r')

    nm = data.readline().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, data.readline().rstrip().split())))

    print("Done with data transport")

    result = arrayManipulation(n, queries)

    print(result)