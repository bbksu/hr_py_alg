from itertools import combinations
def pickingNumbers(a):    
    combs = list(combinations(a, 2))
    comb_dict = dict()    
    for i, x in combs:
        if abs(i -x) == 1:                        
            comb_dict[x, i] = comb_dict.setdefault((x, i),0)+1
    rep = max(comb_dict.values())
    common = []
    for i, x in comb_dict.items():
        if x == rep:
            common = list(i)
            break
    final = 0
    for i in common:
        final += a.count(i)    
    return (final)
    



if __name__ == '__main__':    

    result = pickingNumbers([4,6,5,3,3,1])
    result = pickingNumbers([1, 1, 2,2,4,4,5,5,5])
    result = pickingNumbers([1,2,2,3,1,2])