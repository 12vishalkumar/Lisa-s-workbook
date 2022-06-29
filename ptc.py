import math
import os
import random
import re
import sys
# Complete the 'workbook' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
def workbook(n, k, arr):
    # Write your code here
    res = 0
    page_no = 1
    for index, problem in enumerate(arr):
        p_left = k
        for i in range(1, problem+1):
            if(i == page_no):
                res += 1
            p_left -= 1
            if(p_left == 0):
                p_left = k
                page_no += 1
        if(p_left < k):
            page_no += 1
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = workbook(n, k, arr)
    fptr.write(str(result) + '\n')
    fptr.close()