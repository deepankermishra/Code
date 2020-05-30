"""
http://buttercola.blogspot.com/2018/10/418-sentence-screen-fitting.html

Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.
Note:
A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
"""

def canFit(sentence, times, rows, cols):
	curw, curh = 0, 1
	while times > 0:
		for word in sentence:
			nwd = (curw + 1 if curw else curw) + len(word)
			if nwd > cols:
				curw = len(word)
				curh += 1
			else:
				curw = nwd
			# print(times, curw, curh)
		if curh > rows:
			return False
		times -= 1
	return True

def screenFit(rows, cols, sentence):
	l, h = 0, rows*cols
	ans = 0
	while l <= h:
		m = l + (h-l)//2
		if canFit(sentence, m, rows, cols):
			ans = max(ans, m)
			l = m + 1
		else:
			h = m - 1
	return ans

print(screenFit(2, 8 , ['hello', 'world']))
print(screenFit(rows = 3, cols = 6, sentence = ["a", "bcd", "e"]))
print(screenFit(rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]))



