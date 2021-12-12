# Π19183 Νικήτας Χατζής
# Εφαρμοσμένη συνδυαστική πρώτη σειρά ασκήσεων
# Άσκηση 2

# Ουσιαστικά είναι η ksubsetColexRecC
# απλώς ανανεώνεται η τιμή του αθροίσματος
# πριν κάθε αναδρομική κλήση και γίνεται έλεγχος
# για την τιμή του πριν γίνει εκτύπωση

import time

n=int(input("Εισάγετε το n: "))
k=int(input("Εισάγετε το k: "))
S=int(input("Εισάγετε το S: "))

A = [i for i in range(k+1)] #[0,1,2,...,k]  #σωστή αρχικοποίηση?

s = k*(k+1)/2 #άθροισμα από τη θέση 1 και μετά 1+2+...+κ=κ*(κ+1)/2

count = 0

def askisi2(n,k,s): #not optimal
    global S, count
    if k==n and s==S:
        #print(A[1:])
        count+=1
    elif k!=n:
        askisi2(n-1,k,s)
        if k>0:
            s += n-A[k] #προσθέτουμε τη διαφορά στο άθροισμα
            A[k]=n
            askisi2(n-1,k-1,s)
            s -= n-k    #αφαιρούμε τη διαφορά
            A[k]=k

start = time.time()
askisi2(n,k,s)
end = time.time()
print(count,"items generated")
print("Time elapsed:",end-start,"s")
