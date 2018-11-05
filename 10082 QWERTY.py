from sys import stdin
def main():
    t1 = "`1234567890-="
    t2 = 'QWERTYUIOP[]'
    t3 = "ASDFGHJKL;'"
    t4 = "ZXCVBNM,./"
    while True:
        try:
            entrada = input()
        except EOFError:
            break
        res = ""
        for i in entrada:
            if i == " ":
                res+= " "
            elif i in t1:
                x = t1.index(i)
                res+= t1[x-1]
            elif i in t2:
                x = t2.index(i)
                res+= t2[x-1]                
            elif i in t3:
                x = t3.index(i)
                res+= t3[x-1]                
            elif i in t4:
                x = t4.index(i)
                res+= t4[x-1]
            else:
                res+="]"
        print(res)
main()
