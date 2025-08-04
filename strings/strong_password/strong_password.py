def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong        
    digit = False
    lower = False
    upper = False
    alpha = False
    for i in password:
        digit = any([digit, i.isdigit()])
        lower = any([lower, i.islower()])
        upper = any([upper, i.isupper()])
        alpha = any([alpha, (not i.isalnum())])
    
    chars = [digit, lower, upper, alpha].count(False)
    print([digit, lower, upper, alpha])
    if n >= 6 or n + chars >= 6:
        return (chars)    
    else:        
        return (6 - n)   

if __name__ == '__main__':   
    # n = int(input().strip())
    # password = input()

    n = 3

    password = "Ab1"
    answer = minimumNumber(n, password)
    print(answer)   
    