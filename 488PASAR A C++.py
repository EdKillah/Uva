from sys import stdin
def main():
    casos = int(stdin.readline())
    pos = 1
    for i in range(casos):
        blanco = stdin.readline().strip()
        amplitud = int(stdin.readline())
        frecuencia = int(stdin.readline())
        num = 1
        band = True
        poxi = 1
        for x in range(frecuencia):
            if pos!=casos:
                for aux in range((amplitud*2)):
                    if band:
                        if num>=amplitud:
                            print(str(num)*num)
                            num-=1
                            band = False
                        else:
                            print(str(num)*num)
                            num+=1
                    else:
                        print(str(num)*num)
                        num-=1
            else:
                for aux in range((amplitud*2)):
                    if band:
                        if num>=amplitud:
                            print(str(num)*num)
                            num-=1
                            band = False
                        else:
                            print(str(num)*num)
                            num+=1
                    else:
                        if num!=0 or poxi!=frecuencia:
                            print(str(num)*num)
                        num-=1
                poxi+=1
            band = True
            num=1
        pos+=1
main()
