# Π19183 Νικήτας Χατζής
# Εφαρμοσμένη συνδυαστική πρώτη σειρά ασκήσεων
# Άσκηση 1

#Βασισμένο στη γραμματική
# S -> 0S(n-1,k) | 10S(n-2,k-1) | 1 | ε
#

import time

n = int(input("Μήκος λέξεων: "))
k = int(input("Αριθμός άσσων: "))
B = (n+1)*[None] #store words here, B[0] is dummy value
count = 0

def askisi1(n,k) -> None:
    global count
    if k==0:
        count+=1
        #print(B[1:])   #uncomment to print
    else:
        if k<n:
            B[n]=0
            askisi1(n-1,k)
        if n>=2:
            B[n] = 1
            B[n-1] = 0
            askisi1(n-2,k-1)
        if n==1:    #without this call we lose cases
            B[n]=1
            askisi1(n-1,k-1)

start = time.time()
askisi1(n,k)
end = time.time()
print(count,"items generated.")
print("Time elapsed: ",end-start)
