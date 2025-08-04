def kangaroo(x1, v1, x2, v2):
    jump_1 = set()
    jump_2 = set()
    for i in range(10000):
        x1 += v1
        x2 += v2
        jump_1.add(x1)
        jump_2.add(x2)        
    yes = any(map(lambda x, y: x == y, jump_1, jump_2))
    if yes:
        return ("YES")
    else:
        return ("NO")

kangaroo(0, 3, 4, 2)
kangaroo(0, 2, 5, 3)
kangaroo(2, 1, 1 ,2)