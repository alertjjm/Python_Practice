def solution(numbers, hand):
    answer = ''
    keypad=[[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    left=[3,0]
    right=[3,2]
    for num in numbers:
        if(num==1 or num==4 or num==7):
            left=keypad[num]
            answer+='L'
        elif(num==3 or num==6 or num==9):
            right=keypad[num]
            answer+='R'
        else:
            to=keypad[num]
            ldis=abs(left[0]-to[0])+abs(left[1]-to[1])
            rdis = abs(right[0] - to[0]) + abs(right[1] - to[1])
            if(ldis<rdis):
                left=to
                answer+='L'
            elif(ldis>rdis):
                right=to
                answer+='R'
            else:
                if(hand=='right'):
                    right = to
                    answer += 'R'
                else:
                    left = to
                    answer += 'L'
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))