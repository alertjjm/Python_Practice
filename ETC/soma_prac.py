
def main():
    x = input()
    bomb=0
    lasor=0
    for token in x:
        if(token=='('):
            bomb+=1
        else:
            lasor+=1
    if(bomb==lasor):
        print("YES")
    else:
        print("NO")


if __name__=="__main__":
    main()