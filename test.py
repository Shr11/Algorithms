#reversing an array

arr= [4 , 2 , 8, 6] # using a predefined array
n=4

def revArr(arr):
 
 for i in range(0,int(n/2)):
    t=arr[n-1]
    arr[n-1]=arr[i]
    arr[i]=t
    n=n-1
 print(arr)    
   
revArr(arr) #ERROR