class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_text = re.sub(r'[^a-z0-9]', '',s.lower())
        return stripped_text == stripped_text[::-1]

