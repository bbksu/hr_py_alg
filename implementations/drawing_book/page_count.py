def pageCount(n, p):    
    pages = list(range(0, n+1))
    page_ = list()
    min_pages = list()
    for v, i in enumerate(range(0, n+1,2)):        
        page_.append(v)        
        if p in pages[i:i+2]:             
            min_pages.append(v)              
    page_.reverse()      
    min_pages = min(min_pages)
    print (min(page_.index(min_pages), min_pages))


if __name__ == '__main__':  
    result = pageCount(6, 2)    
    result = pageCount(5, 3)    
    result = pageCount(5, 4)    
    result = pageCount(4, 4)    