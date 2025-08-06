def designerPdfViewer(h, word):    
    tall = 0
    for i in word:
        i = ord(i)
        if i >=97:
            i-=97
        else:
            i-=65        
        tall = max(tall, h[i])    
    return (tall * len(word))

if __name__ == '__main__':      

    result = designerPdfViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5], "abc")
    # result = designerPdfViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5], "ABC")
    result = designerPdfViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7], "zaba")
