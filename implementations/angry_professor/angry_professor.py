def angryProfessor(k, a):    
    late = [max(0, i) for i in a]    
    if late.count(0) < k:
        return ("YES")
    return ("NO")
    

if __name__ == '__main__':   
    result = angryProfessor( 3, [-1,-3,4,2])
    result = angryProfessor(2, [0,-1,2,1])
    result = angryProfessor(3, [-2,-1,0,1,2 ])