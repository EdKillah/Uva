from sys import stdin
def main():
    casos = int(stdin.readline())
    cases = 1
    for entrada in range(casos):
        blank = stdin.readline().strip()
        n = int(stdin.readline())
        l = []
        d = {"A,B,C":"2","D,E,F":"3","G,H,I":"4","J,K,L":"5","M,N,O":"6","P,R,S":"7","T,U,V":"8","W,X,Y":"9"}
        res = {}
        for i in range(n):
            x = stdin.readline().strip()
            l.append(x)
        for i in l:
            aux = ""
            for j in i:
                band = True
                for k in d:
                    if j in k:
                        aux+=d[k]
                        band = False
                if band:
                    if j!="-":
                        aux+=j
            final = aux[:3]+"-"+aux[3:]
            if final in res:
                res[final]+=1
            else:
                res[final] = 1
        absolute = {}
        for i in res:
            if res[i]>1:
                absolute[i] = res[i]
        if len(absolute)==0:
            print("No duplicates.")
        else:
            respuesta = list(absolute.items())
            respuesta.sort(key=lambda x: x[0])
            for i in respuesta:
                print(i[0],i[1])
        if cases!=casos:
            print("")
        cases+=1

main()
