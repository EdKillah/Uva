from sys import stdin
def main():
    n = [int(x) for x in stdin.readline().strip().split()]
    while n!= [0,0]:
        l = []
        for entrada in range(n[1]):
            report = [int(x) for x in stdin.readline().strip().split()]
            l.append(report)
        s = [int(x) for x in range(1,n[0]+1)]
        s = ['*']+s
        #print("S",s)
        for i in l:
            #print("i",i)
            for j in range(i[0],i[1]+1):
                s[j] = '*'
            print("SSS",s)
            cont = 0
            aux = []
            band = True
            ba1=True
            ba2=True
            if s[i[0]-1] != '*':
                aux.append(s[i[0]-1])
                cont+=1
                print("Entro aqui")
                ba1=False
            if i[1]<n[0] and s[i[1]+1]!='*':
                aux.append(s[i[1]+1])
                cont+=1
                print("ENTRO EN ESTEE")
                ba2=False
            print("AUX",aux)
            if ba1 or ba2:
                for j in s[1:]:
                    if j!='*' and j not in aux:
                        if j<=i[0]:
                            #print("entro",j)
                            aux.append(j)
                            cont+=1                            
                        if j>=i[1] and band and j not in aux:
                            aux.append(j)
                            cont+=1
                            band = False
                    if cont>=2:
                        break
            if len(aux)==0:
                print('*','*')
            elif len(aux)==1 and aux[0]>=i[1]:
                print('*',aux[0])
            elif len(aux)==1 and aux[0]<=i[0]:
                print(aux[0],'*')
            else:
                #print("Entra")
                print(aux[0],aux[1])
        print("-")
        n = [int(x) for x in stdin.readline().strip().split()]

main()
