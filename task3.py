inputFile=open('input3.txt','r')
f_line=int(inputFile.readline())
arr=[]
for i in range(f_line):
    i=list(map(int,inputFile.readline().split(' ')))
    arr.append(i)
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half=arr[mid:]
        a1 = mergeSort(left_half)
        a2 = mergeSort(right_half)
        return merge(a1, a2)
def merge(a1, a2):
    out=[]
    i = j  = 0
    # Merge the two halves back together in sorted order
    while i < len(a1) and j < len(a2):
        if a1[i][1] < a2[j][1]:
            out.append(a1[i])
            i += 1
        else:
            out.append(a2[j])
            j += 1
    # Check if any elements were left in the left half
    while i < len(a1):
        out.append(a1[i])
        i += 1
    # Check if any elements were left in the right half
    while j < len(a2):
        out.append(a2[j])
        j += 1
    return out
out=mergeSort(arr)
#Maximum number of tasks
count=1
result=[]
result.append(out[0])
maxi=out[0][1]
for i in range(1,len(out)):
    if maxi<=out[i][0]:
        maxi=out[i][1]
        count+=1
        result.append(out[i])
outputFile = open('output3.txt', 'w')
outputFile.writelines(f'{str(count)}\n')
for j in result:
    outputFile.writelines(f'{str(j[0])} {str(j[1])}\n')
inputFile.close()
outputFile.close()
