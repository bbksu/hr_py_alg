def funnyString(s):    
    s = list(map(ord, s))
    rev_s = []    

    for i in range(len(s)):
        x = s[i:i+2]
        abdiff = abs(x[-1]- x[0])
        if abdiff == 0:
            continue
        rev_s.append(abdiff)
    print(rev_s)
    if (rev_s == rev_s[::-1]):
        return ("Funny")        
    return "Not Funny"


if __name__ == '__main__':
    funnyString("acxz")
    funnyString("bcxz")
    funnyString("lmnop")    
    print(funnyString("ivvkx")    )
    