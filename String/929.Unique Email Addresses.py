'''
Time Complexity: O(C), where C is the total content of emails.

Space Complexity: O(C).
'''
class Solution:
	def numUniqueEmails(self, emails: List[str]) -> int:
		seen = set()

		for email in emails:
			lst = email.split('@')
			localname, domainname = lst[0], lst[1]

			valid_localname = localname.split('+')[0]
			valid_localname = valid_localname.replace('.', '')

			seen.add(valid_localname + '@' + domainname)

		return len(seen)