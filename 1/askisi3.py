# Π19183 Νικήτας Χατζής
# Εφαρμοσμένη συνδυαστική πρώτη σειρά ασκήσεων
# Άσκηση 3

# Βασισμένη στη γραμματική
# S -> 0S0 | 1S1 | 0B1 | ε
# B -> 0B | 1B | ε
#
# πχ B[0]=0, B[n]=0 αναδρομή για 1,n-1 κλπ.


import time

n = int(input("Μήκος λέξεων: "))
B = (n+1)*[None] #store words here, B[0] is dummy value
counter = 0

def Binary(n,s) -> None:    #generate binary words from index n with length s
    global counter
    if n>s:
        counter+=1
        #print(B[1:])    #uncomment to print
    else:
        B[n]=0
        Binary(n+1,s)
        B[n]=1
        Binary(n+1,s)

def askisi3(low,high) -> None:
    global counter
    if low>high:
        counter+=1
        #print(B[1:])   #uncomment to print
    else:
        B[low]=0
        B[high]=0
        askisi3(low+1,high-1)
        if low!=high:
#χωρίς αυτόν τον έλεγχο έβγαζα 2^k duplicates για περιττό n
#με k=ndiv2, όλα συμμετρικά ως προς το ceil(n/2)
            B[low]=1
            B[high]=1
            askisi3(low+1,high-1)
        B[low]=0
        B[high]=1
        Binary(low+1,high-1)


start = time.time()
askisi3(1,n)
end = time.time()
print(counter,"items generated.")
print("Time elapsed: ", end-start, "s")


# Η λύση που δείξατε στη διάλεξη, για σκοπούς ελέγχου αποτελεσμάτων και
# για σύγκριση ταχύτητας.

counter=0    #reset counter
L = len(B)-1 #για την Binary2

def inR(low,high) -> bool:  
    while(low<=high):
        if B[low]<B[high]: return True
        elif B[low]>B[high]: return False
        low,high = low+1,high-1
    return True

def Binary2(n,s) -> None:   #Generate binary words from index n of length s
    global counter
    if n>s and inR(1,L):    #check if extra condition is met
        counter+=1
        #print(B[1:])   #uncomment to print
    elif n<=s:
        B[n]=0
        Binary2(n+1,s)
        B[n]=1
        Binary2(n+1,s)

start = time.time()
Binary2(1,n)
end = time.time()
print(counter,"items generated.")
print("Time elapsed: ", end-start, "s")
