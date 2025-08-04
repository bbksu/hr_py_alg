def birthday(s, d, m):  
    divs = [s[i:m+i] for i in range(len(s))]    
    divs = (map(sum, divs))
    print(len(list(filter(lambda x: x ==d, divs))))

if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))   

    first_multiple_input = input().rstrip().split()
    d = int(first_multiple_input[0])
    

    m = int(first_multiple_input[1])    

    result = birthday(s, d, m)
