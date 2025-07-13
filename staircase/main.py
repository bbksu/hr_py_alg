def stair_case(n):
    # Write your code here    
    for i in range(1, n+1):
        print(" "*(n-i) + "#"*i)

if __name__ == '__main__':
    n = int(input().strip())

    stair_case(n)