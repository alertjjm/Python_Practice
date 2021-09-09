def solution(record):
    answer = []
    userDict={}
    for r in record:
        tokens=r.split()
        if(len(tokens)==3):
            op, uid, nickname = tokens
            if (uid in userDict):
                userDict[uid] = nickname
            else:
                userDict[uid] = nickname
        else:
            op, uid = tokens
        if(op=='Enter'):
            answer.append(uid+"!님이 들어왔습니다.")
        elif(op=='Leave'):
            answer.append(uid+"!님이 나갔습니다.")
    for a in range(len(answer)):
        temp=answer[a]
        uid=temp.split("!")[0]
        temp=temp.replace(uid+"!",userDict[uid])
        answer[a]=temp
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))