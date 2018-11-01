from sys import stdin
def find(x):
    global y
    if y[x]!= x:
        y[x] = find(y[x])
    return y[x]
def union(i,j):
    a = find(i)
    b = find(j)
    if a == b: return
    y[a] = b
    return 

def kruskal(add):
    add.sort()
    print("ADD",add)
    res = 0
    for w,u,v in add:
        if find(u)!=find(v):
            union(u,v)
            res+=w
    return res

def main():
    global y
    n = int(stdin.readline())
    lAdj = []
    y = [i for i in range(n+1)]
    for entrada in range(n-1):
        m = [int(x) for x in stdin.readline().strip().split()]
        lAdj.append([m[2],m[0],m[1]])
    print(lAdj)
    print("Y",y)
    print(kruskal(lAdj))
main()
