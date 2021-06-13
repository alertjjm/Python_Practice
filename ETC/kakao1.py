def solution(s):
    answer = ''
    numberdict={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    l=len(s)
    i=0
    while i<l:
        if(s[i].isdigit()):
            answer+=s[i]
        else:
            start=i
            end=i
            text=s[start]
            while(not s[end].isdigit()):
                end+=1
                text+=s[end]
                if text in numberdict:
                    break
            answer+=numberdict[text]
            i=end+1
            continue
        i+=1
    return int(answer)
def sol2(s):

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))