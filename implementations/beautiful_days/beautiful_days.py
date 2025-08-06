def beautifulDays(i, j, k):
    for i in range(i, j+1):
        day = f"({i}-{int(str(i)[::-1])})/{k}"        
        day = (abs(eval(day)))
        if day == int(day):
            print(i)

if __name__ == '__main__':
    result = beautifulDays(20, 23, 6)