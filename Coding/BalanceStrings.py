"""

https://leetcode.com/problems/replace-the-substring-for-balanced-string/

"""

def balancedString(s):
	chars = 'QWER'
	votes = [0] * 4
	n = len(s)
	for i in range(n):
		c = s[i]
		idx = chars.find(c)
		votes[idx] += 1
	deficit = max(n/4 - votes[0], 0) + max(n/4 - votes[1], 0) + max(n/4 - votes[2], 0) + max(n/4 - votes[3], 0)
	return deficit


print(balancedString('QWER'))
print(balancedString('QWEEQRRW'))
print(balancedString('WQREERWW'))

print(balancedString("WWQQRRR RQQRQ"))
# local deficit = 1 q 1 w 3 e
# global deficit = 1w 3e 

print(balancedString("WWQQRRRRQRWQ"))


       
