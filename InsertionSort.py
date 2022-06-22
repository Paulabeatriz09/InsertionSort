
#Chamando a funcao insertion sort
def insertionSort(array):
    {

    #Percorrer de 1 a 30
    for step in range(1, len(array)):
        key=array[step]
        j=step-1


        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j=j-1

        array[j+1]=key

        }

        {
       while i<=(n+n):
       if i%2!=0
        print(data(i))
        i+=1
        else:
            i+=1
       }



data=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
insertionSort(data)
print('Array em ordem crescente:')
print(data)

