def sockMerchant(n, ar):    
    match = sum(ar.count(i)//2 for i in set(ar))
    return match        

if __name__ == '__main__':   
    # n = int(input().strip())    
    # ar = list(map(int, input().rstrip().split()))
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    result = sockMerchant(n, ar)