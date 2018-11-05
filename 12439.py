from sys import stdin
def main():
    n = int(stdin.readline())
    cases = 1
    for entrada in range(n):
        primera = stdin.readline().strip().split()
        segunda = stdin.readline().strip().split()
        #print(primera)
        #print(segunda)
        d = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October" :10,"November" :11,"December" :12}
        cont = 0
        a1 = int(primera[2])
        a2 = int(segunda[2])
        if len(primera[1])>2:
            d1 = int(primera[1][0:2])
        else:
            d1 = int(primera[1][0])
        if len(segunda[1])>2:
            d2 = int(segunda[1][0:2])
        else:
            d2 = int(segunda[1][0])
        year = a2-a1
        if primera[0] in d:
            m1 = d[primera[0]]
        if segunda[0] in d:
            m2 = d[segunda[0]]
        cont+=year//4
        if (((m2==2 and d2>=29 and a2%4==0) or (m2>2 and a2%4==0)) and ((m1==2 and d1<=29 and a1%4==0 and a1!=a2) or (m1<2 and a1%4==0 and m1!=m2))):
            print("No")
            cont+=1
            
        if ((m2==2 and d2>=29 and a2%4==0 and a1!=a2) or (m2>2 and a2%4==0) or (m1==2 and d1<=29 and a1%4==0) or (m1<2 and a1%4==0 and a2!=a1)): #a2%4==0 and d2>=29 and m2==2
            #cont+=1
            print("Entra")
            #cont+=year//4
            if year//4==0:
                cont+=1
            #cont+=year//4
##            print("1f",cont)
##        if (m2>2 and a2%4==0):
##            cont+=1
##            #cont+=year//4
##            print("2f",cont)
##        if (m1==2 and d1>=29 and a1%4==0):
##            cont+=1
##            #cont+=year//4
##            print("3f",cont)
##        if (m1>2 and a1%4==0):
##            cont+=1
##            #cont+=year//4
##        
##            print("4f",cont)
        print("Case {}:".format(cases),cont)
        cases+=1
        
    
main()
