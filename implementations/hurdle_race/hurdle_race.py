def hurdleRace(k, height):
    potion = max(max(height) - k, 0)    
    return potion


if __name__ == '__main__':       

    result = hurdleRace(4, [1, 6, 3, 5, 2])
    result = hurdleRace(1, [1,2,3,3,2])
    result = hurdleRace(7, [2, 5 ,4,5,2])
