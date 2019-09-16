def Insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:  # asc , desc depends on >,< values.
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j=j-1
    return arr
if __name__=="__main__":
    arr = list(map(int,input("Enter the number").rstrip().split()))
    result=Insertion_sort(arr)
    print(arr)