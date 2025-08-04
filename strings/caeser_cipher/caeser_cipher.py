def caesarCipher(s, k):
    # Write your code here
    print(s)
    counter = 1
    while k > 26:
        counter+=1
        k -= 26
    print(counter)
    cipher = list(map(ord, s))
    f_cipher = []
    print(k)
    for i in cipher:
        if (i >= 65 and i <=90) or (i >= 97 and i <= 122):
            pass

            
        f_cipher.append(i)
    out = ("".join((map(chr, f_cipher))))
    print(out)
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

