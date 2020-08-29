temp=input()
temp=temp.split(" ")
n=int(temp[0])
m=int(temp[1])
def isprime(n):
    if n==1:
        return True
    i=1
    flag=0
    while i*i <=n:
        if(n%i==0):
            flag+=1
        i+=1
    if(flag==1):
        return True
    else:
        return False

for i in range(n,m+1):
    if(isprime(i)):
        print(i)