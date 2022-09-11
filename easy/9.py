def isPalindrome(num: int) -> bool:
    if num < 0:
        return False
    temp = num
    reversed = 0
    while temp != 0:
        reversed = reversed * 10 + temp % 10 
        temp //= 10
    return num == reversed

print(isPalindrome(112))
print(isPalindrome(414))
print(isPalindrome(-14))