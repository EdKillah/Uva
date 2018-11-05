from sys import stdin
def main():
    n = int(stdin.readline())
    while n!= 0:
        l = []
        for i in range(n):
            entrada = [int(x) for x in stdin.readline().strip().split()]
            l.append(entrada)
        band = True
        cont=0
        posc=0
        posf=0
        contfi=0
        contco=0
        aux =0
        for i in l:
            if sum(i)%2!=0:
                band = False
                posf = aux
                cont+=1
                contfi+=1
            aux+=1
        for i in range(n):
            suma=0
            for j in range(n):
                suma+=l[j][i]
            if suma%2!=0:
                band = False
                posc = i
                contco+=1
                cont+=1
        bandaux = True
        if cont==2 and contfi==1 and contco==1:
            bandaux = False
        if band:
            print("OK")
        elif cont>1 and bandaux:
            print("Corrupt")
        else:
            print("Change bit ("+str(posf+1)+","+str(posc+1)+")")
        n = int(stdin.readline())
main()
