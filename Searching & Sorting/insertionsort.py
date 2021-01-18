def insertionsort(arr):
    
    for index in range(1,len(arr)):
        
        currentvalue=arr[index]
        position=index
                            #to check left element  #with right ele i.e currentvalue 
        while position>0 and arr[position-1]>currentvalue:
            arr[position]=arr[position-1]
            position=position-1
        arr[position]=currentvalue


arr=[1,8,7,5,2]
insertionsort(arr)
print(arr)
# print(insertionsort(arr)) ...gives error,'None'
