inputFile = open('input2a.txt', 'r')
N = int(inputFile.readline())
sort1 = inputFile.readline().split(' ')
M = int(inputFile.readline())
sort2 = inputFile.readline().split(' ')
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
    out=[0]*len(a1+a2)
    i = j = k = 0
    # Merge the two halves back together in sorted order
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            out[k] = a1[i]
            i += 1
        else:
            out[k] = a2[j]
            j += 1
        k += 1
    # Check if any elements were left in the left half
    while i < len(a1):
        out[k] = a1[i]
        i += 1
        k += 1
    # Check if any elements were left in the right half
    while j < len(a2):
        out[k] = a2[j]
        j += 1
        k += 1
    return out
arr=list(map(int,sort1+sort2))
out = mergeSort(arr)
outputFile = open('output2a.txt', 'w')
outputFile.writelines(' '.join(map(str, out)))
inputFile.close()
outputFile.close()
