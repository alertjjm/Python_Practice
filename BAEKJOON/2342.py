directions=list(map(int, input().split()))
dplist=[[[0 for i in range(5)],[0 for i in range(5)]] for i in range(len(directions))]
injup={1:[2,4],2:[1,3],3:[2,4],4:[1,3]}
if(len(directions)==1):
    print(0)
elif(len(directions)==2):
    print(2)
else:


    
    '''dplist[0]=2
    st=1
    footset=set()
    footset.add(directions[0])
    for i in range(1,len(directions)-1):
        if(directions[i] in footset):
            dplist[i]=dplist[i-1]+1
        elif(st==1):
            footset.add(directions[i])
            st=0
            dplist[i] = dplist[i - 1] + 2
        else:
            a,b=injup[directions[i]]
            if(a in footset):
                footset.remove(a)
            else:
                footset.remove(b)
            footset.add(directions[i])
            dplist[i] = dplist[i - 1] + 3
    print(dplist[len(directions)-2])'''