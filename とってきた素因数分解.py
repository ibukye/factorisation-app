# https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8

import time

n = int(input(">"))

start = time.time()

def factorization(n):
    arr=[]
    temp=n
    for i in range(2,int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp//=i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

print(factorization(n))

end = time.time()
print(end-start)