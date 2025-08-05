def bonAppetit(bill, k, b):    
    shared = sum(bill)-bill[k]
    charge = b - shared//2
    if charge == 0:
        print("Bon Appetit")
    else:
        print(charge)
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))   

    b = int(input().strip())   
    bonAppetit(bill, k, b)
