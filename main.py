#Define a function named anagramcheck. This function should take two strings as inputs. The output of this function should be a printed message displaying that either the two words are anagrams or they are not. Use at least one dictionary to help you solve this problem.


def anagramcheck(a, b):
	if len(a) != len(b):
		return False

	for x in a:
		if a.count(x) == b.count(x):
			pass
		else:
			return False
		
	
	return True




#Tests
a = anagramcheck('listen', 'silent')
b = anagramcheck('identifiably', 'definability')
c = anagramcheck('here', 'there')
d = anagramcheck('abcd', 'efgh')
f = anagramcheck("elegant man", "a gentleman")
h = anagramcheck("abc", "bcf")

print(a, b, c, d, f, h)

# Anagram Checker with dict for assignment

def anagramcheck(a, b):
	c = {}

	if len(a) != len(b):  # If length is different, it isn't an anagram.
		return False

	for x in a:  # For each character in word a
		if x in c:  # If letter exists in dict
			c[x] += 1  # Increment by 1
		else:  # If value isn't in dict, add to dict with value 1
			c[x] = 1  

	for x in b:  # For each character in word b
		if x in c:  # If letter exists in dict
			c[x] -= 1  # Decrement by 1
		else:  # If value isn't in dict, add to dict with value 1
			c[x] = 1 

	for x in c:  # For each key in the dict
		if c[x] == 0:  # If key equals 0
			pass  # continue through loop
		else:  # If key is not 0, aka one word didn't have same count of chars
			return False
	
	return True
			 
a = anagramcheck('listen', 'silent')
b = anagramcheck('identifiably', 'definability')
c = anagramcheck('here', 'there')
d = anagramcheck('abcd', 'efgh')
f = anagramcheck("elegant man", "a gentleman")
h = anagramcheck("abc", "bcf")
g = anagramcheck("lll", "laa")

print(a, b, c, d, f, h, g)