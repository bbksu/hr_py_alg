def catAndMouse(x, y, z):
    a = abs(z - y)
    b = abs(z - x)    
    if a > b:
        return("Cat A")
    elif a < b:
        return("Cat B")
    else:
        return("Mouse C")


if __name__ == '__main__':    
    result = catAndMouse(1, 2, 3)
    result = catAndMouse(1, 3, 2)
        