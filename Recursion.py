def binary_search_recursive(arr,key,low,high):
    arr.sort(reverse=True)
    if low>high:
        return "Not Found"
    else:
        mid=(low+high)//2
        if key==arr[mid]:
            return True
        elif key<arr[mid]:
            return binary_search_recursive(arr,key,low,mid-1)
        else:
            return binary_search_recursive(arr,key,mid+1,high)
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

if __name__=="__main__":
    key=int(input("enter the key to search"))
    arr=list(map(int,input("Enter the string").rstrip().split()))
    print(binary_search_recursive(arr,key,low=0,high=(len(arr)-1)))
    n=int(input("Enter the no: whose fact & fibo to be found:->"))
    print(fact(n))
    print(fibo(n))
