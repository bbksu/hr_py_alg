def countingValleys(steps, path):    
    sea_level = 0
    valley = 0
    for i in path:
        if i == "U":
            sea_level +=1
            if sea_level ==0:
                valley +=1
        else:
            sea_level -=1    
    return valley

if __name__ == '__main__':      
    result = countingValleys(8, "UDDDUDUU")
    result = countingValleys(8, "DUUUDUDD")
    result = countingValleys(8, "UDUUUDUDDD")
