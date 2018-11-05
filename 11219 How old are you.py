from sys import stdin
def main():
    n = int(stdin.readline())
    case = 1
    for i in range(n):
        blank = stdin.readline().strip()
        current = stdin.readline().strip()
        birth = stdin.readline().strip()
        band1=band2=band3=band4=True
        d1 = int(current[0:2])
        m1 = int(current[3:5])
        y1 = int(current[6:])
        d2 = int(birth[0:2])
        m2 = int(birth[3:5])
        y2 = int(birth[6:])
        year = y1-y2
        month = m1-m2
        day = d1-d2
        #print(year)
        #print(month)
        #print(day)
        if ((day<0 and month<0)):
            year-=1
        if ((d1==d2 and m1==m2 and y1==y2)): #or (((d1==28 and d2==29) or (d1==29 and d2==28)) and (m1==2 and m2==2))) and year<=130):
            print("Case #{}:".format(case),0)
        elif year>130:
            print("Case #{}:".format(case),"Check birth date")
        elif year<=0:
            print("Case #{}:".format(case),"Invalid birth date")
        else:
            #if day<0 or month<0:
                #year-=1
            print("Case #{}:".format(case),year)
        case+=1







    
main()
