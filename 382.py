from sys import stdin
def main():
    n = [int(x) for x in stdin.readline().strip().split()]
    print("PERFECTION OUTPUT")
    for i in n:
        l = []
        if i==0:
            break
        for j in range(1,i):
            if i%j==0:
                l.append(j)
        if i<10:
            if sum(l)==i:
                print("   ",i," PERFECT")
            elif sum(l)>i:
                print("   ",i," ABUNDANT")
            else:
                print("   ",i," DEFICIENT")
        elif i<100:
            if sum(l)==i:
                print("  ",i," PERFECT")
            elif sum(l)>i:
                print("  ",i," ABUNDANT")
            else:
                print("  ",i," DEFICIENT")
        elif i<1000:
            if sum(l)==i:
                print(" ",i," PERFECT")
            elif sum(l)>i:
                print(" ",i," ABUNDANT")
            else:
                print(" ",i," DEFICIENT")
        elif i<10000:
            if sum(l)==i:
                print("",i," PERFECT")
            elif sum(l)>i:
                print("",i," ABUNDANT")
            else:
                print("",i," DEFICIENT")
        else:
            if sum(l)==i:
                print(i," PERFECT")
            elif sum(l)>i:
                print(i," ABUNDANT")
            else:
                print(i," DEFICIENT")            
    print("END OF OUTPUT")
main()
