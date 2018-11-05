from sys import stdin
def main():
    num = int(stdin.readline().strip())
    cases = 1
    for var in range(num):
        n = int(stdin.readline())
        final = n
        aux = str(n)
        x2=0
        if n>=10:
            for i in range(len(aux)):
                x2+=(n%10)**2
                n = n//10
        else:
            x2 = n**2
        suma = 0
        band = True
        while band:
            aux = str(x2)
            suma = x2
            x2 = 0
            for i in range(len(aux)):
                x2+= (suma%10)**2
                suma=suma//10
            if x2<10:
                band=False
                break
            
                
        if x2==1:
            print("Case #{}:".format(cases),final,"is a Happy number.")
        else:
            print("Case #{}:".format(cases),final,"is an Unhappy number.")
        cases+=1
main()
