n=int(input())
if n==1:
    print(1)
else:
    mi=2
    ma=7
    i=1
    while True:
        if n>=mi and n<=ma:
            break
        mi+=6*(i)
        ma+=6*(i+1)
        i+=1
    print(i+1)