M=int(input())
wordDict={}
for i in range(M):
    word=input()
    if (len(word) > 2):
        outerKey=word[0]+word[-1]
        if outerKey in wordDict:
            innerKey=list(word[1:-1])
            innerKey.sort()
            innerKey=''.join(innerKey)
            if innerKey in wordDict[outerKey]:
                wordDict[outerKey][innerKey].append(word)
            else:
                wordDict[outerKey][innerKey]=[word]
        else:
            wordDict[outerKey]={}
            innerKey = list(word[1:-1])
            innerKey.sort()
            innerKey = ''.join(innerKey)
            wordDict[outerKey][innerKey] = [word]
N=int(input())
for i in range(N):
    sentence=input()
    sentence=sentence.split(' ')
    result=1
    for searchWord in sentence:
        if(len(searchWord)>2):
            outerKey=searchWord[0]+searchWord[-1]
            if outerKey in wordDict:
                innerKey = list(searchWord[1:-1])
                innerKey.sort()
                innerKey = ''.join(innerKey)
                if innerKey in wordDict[outerKey]:
                    result=result*len(wordDict[outerKey][innerKey])
    print(result)