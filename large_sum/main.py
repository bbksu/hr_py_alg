def aVeryBigSum(ar):
    # Write your code here
    return sum(ar)
    


ar = map(int, "1000000001 1000000002 1000000003 1000000004 1000000005".split())
result = aVeryBigSum(ar)
print(result)