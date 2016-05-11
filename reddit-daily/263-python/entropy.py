# Reddit Daily Programmer #263 - Calculating Shannon Entropy of a String
# https://www.reddit.com/r/dailyprogrammer/comments/4fc896/20160418_challenge_263_easy_calculating_shannon/

import math

# Solution takes a string 'x', and calculates the Shannon Entropy
def shannonEntropy(x):
	N = len(x);
	count = {}
	
	for val in x:
		# Check if the character was already found
		if val in count:
			count[val] += 1
		else:
			count[val] = 1
	
	H = 0
	for key, val in count.items():
		H += (val/N)*math.log2(val/N)
	
	return -1*H

def testCases():
	print(shannonEntropy("1223334444"))
	print(shannonEntropy("Hello, world!"))
	print(shannonEntropy("122333444455555666666777777788888888"))
	print(shannonEntropy("563881467447538846567288767728553786"))
	print(shannonEntropy("https://www.reddit.com/r/dailyprogrammer"))
	print(shannonEntropy("int main(int argc, char *argv[])"))