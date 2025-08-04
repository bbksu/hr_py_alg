

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here            
    apples = list(map(lambda x: x+a, (apples)))
    oranges = list(map(lambda x: x+b,(oranges)))
    
    apple_dict = dict()    

    for i in range(s, t+1):
        apple_dict[i] = apple_dict.setdefault(i, 0)

    orange_dict = apple_dict.copy()
    
    for i in apples:
        try:
            apple_dict[i] = apple_dict.get(i) + 1
        except:
            continue

    
    for i in oranges:
        try:
            orange_dict[i] = orange_dict.get(i) + 1
        except:
            continue
    
    print(sum(apple_dict.values()))
    print(sum(orange_dict.values()))

    


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()    
    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()   
    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))
    

    oranges = list(map(int, input().rstrip().split()))
    

    countApplesAndOranges(s, t, a, b, apples, oranges)
