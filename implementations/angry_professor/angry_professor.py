def angryProfessor(k, a):
    # Write your code here
    late = [max(0, i) for i in k]
    print(late, late.count(0))
    

if __name__ == '__main__':   
    result = angryProfessor([-1,-3,4,2], 3)
    result = angryProfessor([0,-1,2,1], 2)
    result = angryProfessor([-2,-1,0,1,2 ], 3)