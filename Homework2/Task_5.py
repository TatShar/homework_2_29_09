#Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
#10
#-> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#-> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
import random
ls=list[0,1,2,3,4,5,6,7,8,9]
ls1=[]
i=0
while i>=9:
    index=random.randint(1,10)

    ls1.append(ls[index])
    i+=1
print (ls1)




    
    




