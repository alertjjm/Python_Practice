ipv6=input()
iplist=ipv6.split(":")
if '' in iplist:
    idx=iplist.index('')
while '' in iplist:
    iplist.remove('')
missinglen=8-len(iplist)
if(missinglen!=0):
    for i in range(missinglen):
        iplist.insert(idx,"0000")
for i in range(len(iplist)):
    part=iplist[i]
    iplist[i]="0"*(4-len(part))+part
print(":".join(iplist))