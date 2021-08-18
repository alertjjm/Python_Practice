LS, LP = map(int,input().split())
DNA = input()
a,c,g,t=map(int,input().split())
dnadict = {'A':a, 'C':c, 'G':g, 'T':t}
widnowdict = { 'A':0, 'C':0, 'G':0, 'T':0}
result=0
start=0
for end in range(LS):
    widnowdict[DNA[end]]+=1
    if(end>=LP-1):
        st=True
        for key in widnowdict:
            if(dnadict[key]>widnowdict[key]):
                st=False
                break
        if(st):
            result+=1
        widnowdict[DNA[start]]-=1
        start+=1
print(result)