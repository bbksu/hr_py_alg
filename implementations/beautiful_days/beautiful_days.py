def beautifulDays(i, j, k):
    count = 0
    for i in range(i, j+1):        
        day = (i-int(str(i)[::-1]))/k        
        day = abs(day)
        if day == int(day):
            count += 1    
    return(count)

if __name__ == '__main__':
    result = beautifulDays(20, 23, 6)
    result = beautifulDays(949488, 1753821, 5005440)