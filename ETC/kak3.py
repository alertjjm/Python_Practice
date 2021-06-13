def solution(n, k, cmd):
    stack = []
    # 스택에 삭제한 것들을 저장하자!

    for command in cmd:

        try:
            cm, num = command.split(" ")
        except ValueError:
            cm, num = command, 0

        if cm == "D":
            k += int(num)
        elif cm == "U":
            k -= int(num)
        elif cm == "C":
            stack.append(k)
            n -= 1
            if k == n:
                k = n - 1
        else:
            backup = stack.pop()
            n += 1
            if backup <= k:
                k += 1

    answer = "O" * n
    for idx in stack[::-1]:
        answer = answer[:idx] + "X" + answer[idx:]
    return answer


print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))