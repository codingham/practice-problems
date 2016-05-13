# Reddit Daily Programmer #266 [Hard] - Finding Friends in a Social Graph
# https://www.reddit.com/r/dailyprogrammer/comments/4j65ls/20160513_challenge_266_hard_finding_friends_in/

import easy_266 as easy


# Return a set of v's neighbors using adjacency matrix A
def getNeighbors(A, v):
	Nv = set()
	for i in range(len(A)):
		if A[v][i] and (v-1) != i:
			Nv.add(i)
	
	return Nv


# The BronKerbosch algorithm for finding maximal cliques in a graph
def BronKerbosch(R, P, X, A, C):
	# R, P, and X are the algorithm's recursive sets
	# A is the adjacency matrix for the graph
	# C is passed by reference to all recursive calls -- it is a list of cliques
	
	# Report that a clique has been found, if possible
	if len(P) == 0 and len(X) == 0:
		C.append(sorted(i+1 for i in R))
	
	for v in set(P):
		# Recursive step
		Nv = getNeighbors(A, v)
		BronKerbosch(R | set([v]), P & Nv, X & Nv, A, C)
		
		# Remove v from P and add it to X
		P.remove(v)
		X.add(v)


# Return all maximum sized cliques in a graph using its adjacency matrix
def getMaxCliques(A):
	# Get all cliques
	cliques = []
	BronKerbosch(set(), set(range(len(A))), set(), A, cliques)
	
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
