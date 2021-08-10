def addthree(a, b, c):
    result = str(int(a) + int(b) + int(c))
    if (len(result) == 2):
        return (result[0], result[1])
    else:
        return ("0", result[0])


def addStrings(num1: str, num2: str) -> str:
    L1 = len(num1)
    L2 = len(num2)
    cnt = min(L1, L2)
    adder = "0"
    result = ""
    for i in range(1, cnt + 1):
        adder, base = addthree(adder, num1[-i], num2[-i])
        result = base + result
    if (L1 > L2):
        result = num1[:(L1 - L2)] + result
    else:
        result = num2[:(L2 - L1)] + result
    idx = cnt + 1
    while (adder == "1" and idx <= max(L1, L2)):
        adder, base = addthree(adder, result[-idx], "0")
        result=result[:-idx]+base+result[-idx+1:]
        idx+=1
    if(adder=="1"):
        result="1"+result
    return result


print(addStrings("956", "77"))
print(addStrings("456", "77"))
print(addStrings("0", "0"))