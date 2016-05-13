# Reddit Daily Programmer #266 [Hard] - Finding Friends in a Social Graph
# https://www.reddit.com/r/dailyprogrammer/comments/4j65ls/20160513_challenge_266_hard_finding_friends_in/

import easy_266 as easy


# Return a new list that is the intersection of two lists
def setIntersect(A, B):
	s = [e for e in A if e in B]
	return s


# Return a new list that is the union of two lists
def setUnion(A, B):
	# Find common elements
	s = setIntersect(A, B)
	
	# Initialize final set with all elements of A
	u = [e for e in A]
	
	# Add all remaining elements of B into the final set,
	# using the intersection to prevent adding elements twice
	for e in B:
		if e not in s:
			u.append(e)
	
	return u


# Return a list of v's neighbors using adjacency matrix A
def getNeighbors(A, v):
	Nv = []
	for i in range(len(A)):
		if A[v][i] and (v-1) != i:
			Nv.append(i)
	
	return Nv


# The BronKerbosch algorithm for finding maximal cliques in a graph
def BronKerbosch(R, P, X, A, C):
	# R, P, and X are the algorithm's recursive sets
	# A is the adjacency matrix for the graph
	# C is passed by reference to all recursive calls -- it is a list of cliques
	
	# Report that a clique has been found, if possible
	if len(P) == 0 and len(X) == 0:
		C.append([i+1 for i in R])
	
	for v in P:
		# Recursive step
		Nv = getNeighbors(A, v)
		BronKerbosch(setUnion(R,[v]), setIntersect(P,Nv), setIntersect(X,Nv), A, C)
		
		# Remove v from P and add it to X
		P = [i for i in P if i != v]
		X.append(v)


# Return all maximum sized cliques in a graph using its adjacency matrix
def getMaxCliques(A):
	# Get all cliques
	cliques = []
	BronKerbosch([], list(range(len(A))), [], A, cliques)
	
	# Determine the clique with the largest connectivity
	max_conn = max(len(L) for L in cliques)
	
	# Pull out the cliques with the maximum connectivity
	return [L for L in cliques if len(L) == max_conn]


# Automatically load and test a graph for this challenge
def test(filename):
	# Load file and generate the adjacency matrix
	num_nodes, edges = easy.load(filename)
	adj = easy.adjacency(num_nodes, edges)
	
	# Print out all maximum sized cliques in the graph
	print(getMaxCliques(adj))
