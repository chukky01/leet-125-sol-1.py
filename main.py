class Solution:
  def isPalindrome(self, s: str) -> bool:
    newStr = ""

    for c in s: # You could also say for char in s, but just make sure you stay constant with whichever one you pick
      if c.isalnum():
        newStr += c.lower()
    return newStr == newStr[::-1]
