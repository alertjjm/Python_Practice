# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    segs = []
    for i in range(len(A)):
        segs.append([A[i],B[i]])
    segs.sort(key=lambda x:(x[1],x[0]))
    last=-1
    cnt=0
    for start,end in segs:
        if(start>last):
            cnt+=1
            last=end
    return cnt

print(solution([1,3,7,9,9],[5,6,8,9,10]))
print(solution([0],[0]))