# Reddit Daily Programmer #267 [Easy] - All the places your dog didn't win
# https://www.reddit.com/r/dailyprogrammer/comments/4jom3a/20160516_challenge_267_easy_all_the_places_your/


def place(num):
	ones = num % 10
	postfix = ""
	
	if ones == 0 or ones > 3 or num in range(11, 14):
		postfix = "th"
	elif ones == 3:
		postfix = "rd"
	elif ones == 2:
		postfix = "nd"
	else:
		postfix = "st"
	
	return str(num) + postfix


def otherPlaces(pos, max_pos):
	return ", ".join(place(i) for i in range(1,max_pos+1) if i != pos)
