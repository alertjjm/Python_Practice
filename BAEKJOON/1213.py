name=input()
alphadict={}
for ch in name:
    if ch in alphadict:
        alphadict[ch]+=1
    else:
        alphadict[ch]=1
alphabets=list(alphadict.keys())
alphabets.sort()
newname=""
status=False
for alpha in alphadict:
    if (alphadict[alpha] % 2 == 1):
        status=True
        break
if status:
    middle=-1
    cnt=0
    for alpha in alphadict:
        if(alphadict[alpha]%2==1):
            middle=alpha
            cnt+=1
    if(cnt>1):
        print("I'm Sorry Hansoo")
    else:
        for alph in alphabets:
            num = alphadict[alph]
            for i in range(num // 2):
                newname += alph
        revnewname = newname
        s_list = list(revnewname)
        s_list.reverse()
        revnewname = ''.join(s_list)
        print(newname + middle+revnewname)
else:
    for alph in alphabets:
        num=alphadict[alph]
        for i in range(num//2):
            newname+=alph
    revnewname=newname
    s_list = list(revnewname)
    s_list.reverse()
    revnewname=''.join(s_list)
    print(newname+revnewname)