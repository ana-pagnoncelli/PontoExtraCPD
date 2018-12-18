import time

def insertionsort(A):
    comparacoes = 0
    trocas = 0
    start_time = time.time()
    #we start loop at second element (index 1) since the first item is already sorted
    for j in range(1,len(A)):
        key = A[j] #The next item we are going to insert into the sorted section of the array

        i = j-1 #the last item we are going to compare to
        #now we keep moving the key back as long as it is smaller than the last item in the array
        
        comparacoes = comparacoes + 1
        while (i > -1) and key < A[i]: #if i == -1 means that this key belongs at the start
            A[i+1]=A[i] #move the last object compared one step ahead to make room for key
            trocas = trocas + 1
            i=i-1 #observe the next item for next time.
            comparacoes = comparacoes + 1
        #okay i is not greater than key means key belongs at i+1
        if(i<=-1):
            comparacoes = comparacoes - 1
        A[i+1] = key
        trocas = trocas + 1
        if (time.time() - start_time) > 3600:
            return A, comparacoes, trocas, '*'
    end_time = (time.time() - start_time)*1000
    return A, comparacoes, trocas, end_time
