from sys import stdin
def main():
    n = stdin.readline().strip()
    while n!= "":
        x = int(n)
        aux = [int(i) for i in stdin.readline().strip().split()]
        cont = 0
        for var in aux:
            if var == x:
                cont+=1
        print(cont)
        n = stdin.readline().strip()
main()
