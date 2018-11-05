from sys import stdin
def main():
    n = int(stdin.readline())
    case = 1
    while n>=0:
        meses = [int(x) for x in stdin.readline().strip().split()]
        necesarios = [int(x) for x in stdin.readline().strip().split()]
        cont = n
        band = True
        print("Case {}:".format(case))
        if necesarios[0]<=n:
            print("No problem! :D")
        else:
            print("No problem. :(")
        cont+=meses[0]
        
        for i in range(1,len(necesarios)):
            #cont+=meses[i]
            #print("necesarios", necesarios[i])
            #print("cont",cont)
            if cont>=necesarios[i]:
                cont-=necesarios[i]
                #print("cont ENTRO",cont)
                print("No problem! :D")
            else:
                print("No problem. :(")
            cont+=meses[i]
                
        n = int(stdin.readline())
        case+=1
main()
