temp=input()
temp=temp.split(" ")
n=int(temp[0])
m=int(temp[1])
chess=[]
minimum=60*60
def counting(temp):
    count1=0
    count2=0
    #start with W
    for i in range(8):
        if i%2==0:
            for j in range(8):
                if j%2==0 and temp[i][j]=='B':
                    count1+=1
                elif j%2==1 and temp[i][j]=='W':
                    count1+=1
        else:
            for j in range(8):
                if j%2==0 and temp[i][j]=='W':
                    count1+=1
                elif j%2==1 and temp[i][j]=='B':
                    count1+=1
    #start with B
    for i in range(8):
        if i%2==0:
            for j in range(8):
                if j%2==0 and temp[i][j]=='W':
                    count2+=1
                elif j%2==1 and temp[i][j]=='B':
                    count2+=1
        else:
            for j in range(8):
                if j%2==0 and temp[i][j]=='B':
                    count2+=1
                elif j%2==1 and temp[i][j]=='W':
                    count2+=1
    return min(count1,count2)
for i in range(n):
    temp=input()
    temp=list(temp)
    chess.append(temp)
for i in range(n-8+1):
    for j in range(m-8+1):
        temp=chess[i:i+8]
        for k in range(8):
            temp[k]=temp[k][j:j+8]
        n=counting(temp)
        if n<minimum:
            minimum=n
print(minimum)
