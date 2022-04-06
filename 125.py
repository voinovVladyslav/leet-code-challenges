def isPalindrome(s: str) -> bool:
    s = s.lower()
    for i in set(s):
        if not i.isalpha() and not i.isnumeric():
            s = s.replace(i, '')
    
    return s == s[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))