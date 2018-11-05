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
        for i in l:
            for j in range(i[0],i[1]+1):
                s[j] = '*'
            aux = []
            cont=0
            if s[i[0]-1]=='*':
                var = i[0]
                for j in range(i[0]):
                    if s[i[0]-j]!='*':
                        aux.append(s[i[0]-j])
                        break
            else:
                aux.append(s[i[0]-1])
            for j in range(i[1],n[0]+1):
                if s[j]!= '*':
                    aux.append(j)
                    break
            if len(aux)==0:
                print('*','*')
            elif len(aux)==1 and aux[0]>=i[1]:
                print('*',aux[0])
            elif len(aux)==1 and aux[0]<=i[0]:
                print(aux[0],'*')
            else:
                print(aux[0],aux[1])
        print("-")
        n = [int(x) for x in stdin.readline().strip().split()]

main()
