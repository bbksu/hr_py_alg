def breakingRecords(scores):
    # Write your code here
    high = scores[0]
    low = high
    h_list = []
    l_list = []
    for i in scores:
        if i > high:
            high = i
            h_list.append(high)
        if i < low:
            low = i
            l_list.append(low)

    return " ".join([h_list.__len__().__str__(), l_list.__len__().__str__()])

if __name__ == '__main__':    
    # n = int(input().strip())
    n = 9

    # scores = list(map(int, input().rstrip().split()))
    scores = [10,5,20,20,4,5,2,25,1]
    # scores = [3,4,21,36,10,28,35,5,24,42]

    result = breakingRecords(scores)
    print(result)
