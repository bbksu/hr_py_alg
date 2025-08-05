from itertools import product

def getMoneySpent(keyboards, drives, b):
    cart_product = product(keyboards, drives)
    price = map(sum, cart_product)  
    cost = [i if i <= b else -1  for i in price]    
    cost = max(cost)    
    return (cost)
        

if __name__ == '__main__':    
    moneySpent = getMoneySpent([3, 1], [5, 2, 8], 10)