from sys import stdin
def main():
    n = int(stdin.readline())
    while n!= 0:
        y = [int(x) for x in stdin.readline().strip().split()]
        y.sort()
        print(y)
        y.reverse()
        print(y)
        aux = ""
        for i in y:
            aux+=str(i)
        print(aux)
        n = int(stdin.readline())
    

    
main()
