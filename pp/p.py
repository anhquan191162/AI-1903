def main(n,m):
    temp = [0]*(n+1)
    for i in range(n):
        temp[m[i]-1] = 1
    for i in range(n+1):
        if temp[i] == 0:
            return i + 1

if __name__ == "__main__":
    n = int(input())
    m = list(map(int,input()))
    print(main(n,m))
