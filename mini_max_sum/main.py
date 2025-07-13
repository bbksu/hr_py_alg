#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def mini_max_sum(arr):
    # Write your code here
    arr = sorted(arr)
    print(sum(arr[:-1]), end=" ")
    print(sum(arr[1:]))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    mini_max_sum(arr)
    
