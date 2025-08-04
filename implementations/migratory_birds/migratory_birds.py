def migratoryBirds(arr):
    # Write your code here
    bird_dict = dict()
    for i in arr:
        bird_dict[i] = bird_dict.setdefault(i, 0)+1   
    birds = []
    for i in bird_dict.items():
        if i[1] == max(bird_dict.values()):
            birds.append(i[0])

    return min(birds)

if __name__ == '__main__':    

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    
    result = migratoryBirds(arr)

    