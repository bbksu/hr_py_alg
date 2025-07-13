
def compareTriplets(a, b):
    # Write your code here
    first = 0
    second = 0
    for i in zip(a,b ):
        if i[0] > i[1]:
            first += 1
        elif i[0] < i[1]:
            second += 1        
    return [first, second]

if __name__ == '__main__':  
    
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))    
    result = compareTriplets(a, b)
    print(result)