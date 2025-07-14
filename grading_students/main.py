# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    # grades = [80, 73, 67, 38, 33]
    final = []
    for i in grades:        
        if i < 38 or i % 5 == 0:
            final.append(i)
        else:
            k = i            
            for j in [1]*2:
                k += j
                if k % 5==0:
                    final.append(k)
                    break
            else:
                final.append(i)            
            
    return final


if __name__ == '__main__':    

    # grades_count = int(input().strip())

    grades = []

    # for _ in range(1):
    #     grades_item = int(input().strip())
    #     grades.append(grades_item)
    print()
    result = gradingStudents([])

    
