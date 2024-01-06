inputFile=open('input1b.txt','r')
f_line=list(map(int,inputFile.readline().split(' ')))
s_line=list(map(int,inputFile.readline().split(' ')))
left,right,target=0,f_line[0]-1,f_line[1]
out=[]
flag=False
while left<right:
    sum=s_line[left]+s_line[right]
    if sum<target:
        left+=1
    elif sum>target:
        right-=1
    elif sum==target:
        out.append(left+1)
        out.append(right+1)
        flag=True
        break
if flag==False:
    out.append('Impossible')
outputFile=open('output1b.txt','w')
outputFile.writelines(' '.join(map(str,out)))
inputFile.close()
outputFile.close()