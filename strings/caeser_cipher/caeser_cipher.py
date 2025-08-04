def caesarCipher(s, k):    
    cipher = list(map(ord, s))    
    f_cipher =[]
    for i in cipher:
        if (i >= 65 and i <=90) or (i >= 97 and i <= 122):
            if chr(i).isupper():
                i +=10
                if not (i >= 65 and i <=90):
                    i-=26
            else:
                i+=10
                if not (i >= 97 and i <= 122):
                    i-=26
        f_cipher.append(i)
    out = ("".join((map(chr, f_cipher))))    
    return out

if __name__ == '__main__':    

    # n = int(input().strip())

    # s = input()
    s = "middle-Outz"

    # k = int(input().strip())
    k = 2

    result = caesarCipher(s, k)
    result = caesarCipher("abcdefghijklmnopqrstuvwxyz", 3)
    result = caesarCipher("There's-a-starman-waiting-in-the-sky", 3)
    result = caesarCipher("!m-rB`-oN!.W`cLAcVbN/CqSoolII!SImji.!w/`Xu`uZa1TWPRq`uRBtok`xPT`lL-zPTc.BSRIhu..-!.!tcl!-U", 62)

