n=int(input())
if(n%2==0):
    string="* "*(n//2)
    string=string[:-1]
    string=string+"\n"+" "+string
    for i in range(n):
        print(string)
else:
    string1 = "* " * ((n+1) // 2)
    string1 = string1[:-1]
    string2 = "* " * ((n - 1) // 2)
    string2 = string2[:-1]
    string=string1+"\n "+string2
    for i in range(n):
        print(string)

