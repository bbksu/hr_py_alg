
from itertools import combinations

def divisibleSumPairs(n, k, ar):
    # Write your code here
    ar.sort()
    counter= 0
    for i in map(lambda x: sum(x),list(combinations(ar, 2))):
        if i % k == 0:
            counter +=1    
    return counter

if __name__ == '__main__':


    # first_multiple_input = input().rstrip().split()
    first_multiple_input = [6, 3]

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    # ar = list(map(int, input().rstrip().split()))
    ar = [1, 3,2,6,1,2]

    result = divisibleSumPairs(n, k, ar)
