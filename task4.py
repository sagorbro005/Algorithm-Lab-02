inputFile=open('input4.txt','r')
f_line=list(map(int,inputFile.readline().split(' ')))
N=f_line[0] #Number of tasks
M=f_line[1] #Number of people
arr=[]
for i in range(N):
    i=list(map(int,inputFile.readline().split(' ')))
    arr.append(i)   #Storing all tasks in a list
#Sorting the list in ascending order by their end times
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left_half = arr[:mid]   #Split the list into two halves
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
maxi=out[0][1]  #Taking the first sorted end time as maximum value by default
count=1 #As we already taken a value in maxi so our count will start from 1
i=0
while i<M:
  if len(out)==1:   #If there is anyone left with any task, then the taks will be assigned to him
    count+=1
    break
  j=1
  flag=False
  while j<len(out):
    if maxi==out[j][0]: #Checking first no gap between two tasks in sorted order
      maxi=out[j][1]
      count+=1
      out.pop(j)    #If a task is assigned to someone then the task will be removed from the list
      j-=1
    j+=1
  # if flag==True:    #If the condition is true then the following will be changed.
  #   out.pop(0)  #First task was already assigned to someone so it will be removed.
  #   i+=1
  #   maxi=out[0][1]  #Second element(end time) of the list will now the maximum.
  if flag==False and i==0:
    count-=1
  k=1
  while k<len(out):
    if maxi<=out[k][0]: #Secondly,it the start time is greater or equal to the maxi then the task will be assigned to someone
      maxi=out[k][1]
      count+=1
      out.pop(k)
      k-=1
    k+=1
  count+=1
  out.pop(0)
  maxi=out[0][1]
  i+=1
outputFile=open('output4.txt','w')
outputFile.writelines(str(count))
inputFile.close()
outputFile.close()