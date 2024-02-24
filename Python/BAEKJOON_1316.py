count=0
for i in range(int(input())):
    word=list(input())
    word2=[]
    for j in range(1,len(word)):
        if(word[j-1]==word[j]):
            word2.append(word[j])
    for k in word2:
        word.remove(k)
    word3=set(word)
    if(len(word3)==len(word)):
        if(len(word)!=0):
            count+=1
print(count)