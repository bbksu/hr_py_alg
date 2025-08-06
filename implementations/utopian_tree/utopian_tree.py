def utopianTree(n):    
    length = 1
    for i in range(n):
        if i % 2 !=0:
            length+=1
        else:
            length *=2
    return (length)

if __name__ == '__main__':    
    result = utopianTree(0)
    result = utopianTree(1)
    result = utopianTree(4)

        
