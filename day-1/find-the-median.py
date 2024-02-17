
#!/bin/python3
"""
The median of a list of numbers is essentially its middle element after sorting. The same number of elements occur after it as before. Given a list of numbers with an odd number of elements, find the median?

Example

The sorted array . The middle element and the median is .

Function Description

Complete the findMedian function in the editor below.

findMedian has the following parameter(s):

int arr[n]: an unsorted array of integers
Returns

int: the median of the array
Input Format

The first line contains the integer , the size of .
The second line contains  space-separated integers 

Constraints

 is odd
Sample Input 0

7
0 1 2 4 6 5 3
Sample Output 0

3
Explanation 0

The sorted . It's middle element is at .
"""
import math
import os
import random
import re
import sys

#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    arr = sorted(arr)
    return arr[len(arr)//2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()