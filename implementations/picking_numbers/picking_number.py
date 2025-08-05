from itertools import combinations, product
def pickingNumbers(a):
    # Write your code here
    a.sort()    
    combs = list(combinations(a, 2))
    comb_dict = dict()
    print(combs)    
    for i in combs:
        comb_dict[i] = comb_dict.setdefault(i, 0)+1
    max_val = max(comb_dict.values())

    for i, y in comb_dict.items():
        if y == max_val:
            print(i)

    print(comb_dict)           



if __name__ == '__main__':    

    result = pickingNumbers([4,6,5,3,3,1])
    # result = pickingNumbers([1, 1, 2,2,4,4,5,5,5])