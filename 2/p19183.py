#
#P19183
#ASK2

import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#1)

#Create a random graph with n nodes and k edges

def ksubsetRand(B,n,k): #random Bn,k
    m=1
    while k>0:
        U = random.uniform(0,1)
        if n*U<k:
            B[m]=1
            k-=1
        m+=1
        n-=1
    return B


def graphMatrix(B,n):   #return adjacency matrix
    a = np.zeros((n,n))
    c=0
    for i in range(n):
        for j in range(i+1,n):
            a[i,j] = B[c]
            a[j,i] = B[c]
            c+=1
    return a.astype(int)


n = int(input("Enter number of nodes: "))
n2 = int(n*(n-1)/2) #size of upper triangle
k = int(input("Enter number of edges: "))
if k<0 or k>n2:
    print("k must be between 0 and C(n,k)")

B = [0 for i in range(n2+1)]
B = ksubsetRand(B,n2,k) #random Bn2,k
print("ΠΡΩΤΟ ΕΡΩΤΗΜΑ")
print("Graph as Bn,k: ",B[1:])
adj_matrix = graphMatrix(B[1:],n)   #adjacency matrix from Bn2,k
print("Adj. matrix of graph: ")
print(adj_matrix)
G = nx.convert_matrix.from_numpy_matrix(adj_matrix) #graph from adjacency matrix

#2)

#Generate all cliques of a given graph.
#Av = vertices adjacent to v
#Bv = vertices larger than v
#Cl = Axl-1 TOMH Bxl-1 TOMH Cl-1(Choice set)
#C0=V


def ComputeA(G,v):
    return {n for n in G.neighbors(v)}

def ComputeB(G,v):
    return {n for n in range(v+1,len(G.nodes()))}

#store G.nodes() as set
node_set = set(G.nodes())

A,B = [],[]
for i in range(n):
    A.append(ComputeA(G,i))
    B.append(ComputeB(G,i))

N = [set() for i in range(n+1)] #initialize as empty
C = [set() for i in range(n+1)] #initialize as empty
X = [None for i in range(n)]

def AllCliques(l):  #print all cliques
    if l==0: print([])
    else: print(X[:l])
    if l==0: N[l] = node_set
    else: N[l] = A[X[l-1]].intersection(N[l-1])
    if(N[l]==set()): print("maximal")
    if l==0: C[l] = node_set
    else: C[l] = A[X[l-1]].intersection(B[X[l-1]],C[l-1])   
    for x in C[l]:
        X[l] = x
        AllCliques(l+1)

print("ΔΕΥΤΕΡΟ ΕΡΩΤΗΜΑ")
AllCliques(0)   #find all cliques

#3) CAN BE PASTED ABOVE 2) TO RUN BEFORE 2)

#estimate rec tree size
node_list = list(G.nodes())
neighbors = [list(G.neighbors(v)) for v in G.nodes] #prepare neighbors list
for nei in neighbors:
    nei.append(None)


def ComputeC2(x,path):
    #find valid next nodes after x for path
    if x==path[0] and x!=None:  #if first node after ∅ return all larger neighboors
        return [n for n in neighbors[x] if n==None or n>x]
    elif x==None:   #if end of path return empty list
        return []
    else:   #else return all larger neighbors that are not in path
        #and have every element of path as neighbor
        c = [n for n in neighbors[x] if n==None or n>x]
        index = path.index(x)
        for n in reversed(path[:index]):
            if n in c:
                c.remove(n)
        for i in c:
            for p in path:
                if i!=None and p not in neighbors[i]:
                    c.remove(i)
        return c

def EstimateTreeSize():
    s=1
    N=1
    l=0
    C2 = [[]]
    path = []
    C2[0] = node_list
    #C2[0].append(None)
    while C2[l]!=[]:
        c = len(C2[l])
        s = c*s
        N = N+s
        x = random.choice(C2[l])
        path.append(x)
        l = l+1
        C2.append(ComputeC2(x,path))
    return N,path

s=0
X=0
for i in range(10):
    X,path = EstimateTreeSize()
    #print("Iteration ",i+1)
    #print("Path: ",path)
    #print("Est size: ",X)
    s+=X

print("ΤΡΙΤΟ ΕΡΩΤΗΜΑ")
print("Average est. size: ",float(s/10))
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()  #show graph

