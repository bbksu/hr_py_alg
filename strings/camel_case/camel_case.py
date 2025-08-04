def camelcase(s):
    # Write your code here
    count = 1
    for i in s:
        if str(i).isupper():            
            count +=1            
    return count

if __name__ == '__main__':
    

    s = input()
    # s = "saveChangesInTheEditor"    

    result = camelcase(s)

