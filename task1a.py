inputFile=open('input1a.txt','r')
f_line=list(map(int,inputFile.readline().split(' ')))
s_line=list(map(int,inputFile.readline().split(' ')))
count,target=f_line[0],f_line[1]
out=[]
flag=False
for i in range(count):
    for j in range(i+1,count):
        sum=s_line[i]+s_line[j]
        if sum==target:
            out.append(i+1)
            out.append(j+1)
            flag=True
            break
if flag==False:
    out.append('Impossible')
outputFile=open('output1a.txt','w')
outputFile.writelines(' '.join(map(str,out)))
inputFile.close()
outputFile.close()