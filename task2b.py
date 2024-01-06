inputFile=open('input2b.txt','r')
count1=int(inputFile.readline())
list1=list(map(int,inputFile.readline().split(' ')))
count2=int(inputFile.readline())
list2=list(map(int,inputFile.readline().split(' ')))
pointer1,pointer2=0,0
out=[]
while pointer1<count1 and pointer2<count2:
    if list1[pointer1]<list2[pointer2]:
        out.append(list1[pointer1])
        pointer1+=1
    else:
        out.append(list2[pointer2])
        pointer2+=1
while pointer1<count1:
    out.append(list1[pointer1])
    pointer1+=1
while pointer2<count2:
    out.append(list2[pointer2])
    pointer2+=1
outputFile=open('output2b.txt','w')
outputFile.writelines(' '.join(map(str,out)))
inputFile.close()
outputFile.close()

