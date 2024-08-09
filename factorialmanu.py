import time
import math

n = int(input('number: '))

start = time.time()
tmp= n
num = 1
while tmp>1:
    tmp/=num
    num+=1
    if tmp<=1:
        print(num-1)
        end=time.time()
        #print(end-start)


def factorial(n):
    i=1
    while math.factorial(i)<n:
        i+=1
        if math.factorial(i)==n:
            print(f'{n} is a factorial number{i}')
            break
        elif math.factorial(i)>n:
            print(f'factorial number:{i}')
            break
        
start1 = time.time()
factorial(n)
end1 = time.time()
#print(end1-start1)

print((end-start)<(end1-start1))