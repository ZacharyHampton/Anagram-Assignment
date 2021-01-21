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

	for x in a:
		if x in c:
			c[x] += 1
		else:
			c[x] = 1

	for x in b:
		if x in c:
			c[x] += 1
		else:
			c[x] = 1

	for x in c:
		if c[x] % 2 == 0:
			pass
		else:
			return False
	
	return True
			 
a = anagramcheck('listen', 'silent')
b = anagramcheck('identifiably', 'definability')
c = anagramcheck('here', 'there')
d = anagramcheck('abcd', 'efgh')
f = anagramcheck("elegant man", "a gentleman")
h = anagramcheck("abc", "bcf")

print(a, b, c, d, f, h)