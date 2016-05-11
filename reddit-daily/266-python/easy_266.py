# Reddit Daily Programmer #266 [Easy] - Basic Graph Statistics: Node Degrees
# https://www.reddit.com/r/dailyprogrammer/comments/4ijtrt/20160509_challenge_266_easy_basic_graph/

# Python 3.5
# Both the main challenge and bonus solution require two arguments:
# - N, the number of nodes
# - edges, a list containing tuples of nodes where each node is a number 1 to N
# The extra function imports data from a text file and calls both the degree
# and adjacency functions


# Challenge -- returns an N element list representing the degree of each node
def degree(N, edges):
	# Initialize a list to hold edge connections to each node
	counter = [0]*N
	
	# Increment the degree of both the left and right node in the tuple
	# Nodes have to be decremented because the list indices are 0 to N-1
	for (node_L, node_R) in edges:
		counter[node_L-1] += 1
		counter[node_R-1] += 1
	
	return counter


# Bonus -- returns an N-by-N matrix (as an N element list of N element lists) 
# representing the adjacency of each node
def adjacency(N, edges, directed=False):
	# Create a 2 dimensional array using lists to hold the matrix
	adjacency = [[0]*N for i in range(N)]
	
	# Iterate through all edges and update the matrix
	for (node_L, node_R) in edges:
		adjacency[node_L-1][node_R-1] += 1
		
		if not directed:
			adjacency[node_R-1][node_L-1] += 1
	
	return adjacency


# Helper function to import formatted graph data from a file
def load(filename):
	# Read in data from a file with the format given on reddit
	data = open(filename, 'r')
	num_nodes = int(data.readline())
	edges = []
	
	input = data.readline()
	while input != "":
		N1, N2 = [int(x) for x in input.split()]
		edges.append( (N1,N2) )
		input = data.readline()
	
	data.close()
	
	return (num_nodes, edges)


# Test function that will import data, call the functions, and print the results
def test(filename):
	num_nodes, edges = load(filename)
	
	# Test degree function
	degrees = degree(num_nodes, edges)
	
	for i in range(num_nodes):
		print("Node", i+1, "has a degree of", degrees[i])
	
	# Test adjacency function
	adj = adjacency(num_nodes, edges)
	
	for i in range(num_nodes):
		for j in range(num_nodes):
			print(adj[i][j], ' ', end="")
		
		print()