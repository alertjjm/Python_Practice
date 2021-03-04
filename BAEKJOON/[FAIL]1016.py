import math
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
minnum,maxnum=map(int, input().split())
def squarenono(x):
    cnt=x
    for i in range(2, int(math.sqrt(x)) + 1):
        if(is_prime_number(i)):
            temp=i*i
            cnt-=cnt//temp
    return cnt
result=squarenono(maxnum)-squarenono(minnum)
print(result)