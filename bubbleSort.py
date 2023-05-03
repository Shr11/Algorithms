def bubSort(arr):
    n=len(arr)

    #optimizing to reduce the no of passes if already sorted
    swapped = False

    #for passes
    for i in range(n-1):
        
        #for comparisons
        for j in range (n-1-i):

            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j] , arr[j + 1] = arr[j + 1] , arr[j]

        if swapped == False:
                return
        
    #driver code
    arr = [2,6,5,7,8,9]
    bubSort(arr)
    print(arr)
