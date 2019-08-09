def binary_search(arr,key):
    arr.sort(reverse=False) # Sort's array in ascending order.
    low=0
    high=len(arr)-1
    while low<=high:
        mid =(low+high)//2
        if arr[mid]==key:
            return "Found"
        elif key<arr[mid]:
            high=mid-1
        else:               # It's obvious that Key>arr[mid]
            low=mid+1
    return "Not Found"
if __name__=="__main__":
    key=int(input("enter the key to search->"))
    arr=list(map(int,input("Enter the string->").rstrip().split()))
    print(binary_search(arr,key))
