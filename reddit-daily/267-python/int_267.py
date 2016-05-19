from sympy import Matrix

def eqResistorMesh(filename, Rtest=1000.0):
	# Import mesh from file
	with open(filename, 'r') as f:
		# First line has all the node names
		V = f.readline().split()
		
		# Create neighbor lists for each node from the connections in the file
		adj = {v: {} for v in V}
		for line in f.readlines():
			edge = line.split()
			
			# If two nodes are connected by two (or more) parallel resistors, simplify
			if edge[1] in adj[edge[0]]:
				adj[edge[0]][edge[1]] = 1.0 / ( 1.0/adj[edge[0]][edge[1]] + 1.0/float(edge[2]) )
				adj[edge[1]][edge[0]] = adj[edge[0]][edge[1]]
			else:
				adj[edge[0]][edge[1]] = float(edge[2])
				adj[edge[1]][edge[0]] = float(edge[2])
	
	# Connect a test node to the first node with a known series resistance
	V.sort()
	adj['TEST'] = {V[0]: Rtest}
	adj[V[0]]['TEST'] = Rtest
	V.insert(0, 'TEST')
	
	# Generate a matrix that will be used to solve for node voltages
	N = len(adj)
	A = Matrix.zeros(N, N+1)
	
	# Test node has a known voltage (of 1V)
	A[0, 0] = 1.0
	A[0, N] = 1.0
	
	# Last node has a known voltage (of 0V)
	A[N-1, N-1] = 1.0
	
	# Populate matrix using KCL: sum of all currents in/out of a node = 0
	for i in range(1, N-1):
		for key in adj[V[i]]:
			A[i, V.index(key)] = -1.0/adj[V[i]][key]
			A[i, i] += 1.0/adj[V[i]][key]
	
	# Get matrix in reduced row echelon form, get the node voltages,
	# and calculate Req with Va=I*Req where the I is the current through the test resistor
	solved = A.rref()[0].col(N)
	return (Rtest*solved[1])/(solved[0]-solved[1])
