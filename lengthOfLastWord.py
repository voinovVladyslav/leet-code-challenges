def lenghtOfLastWord(s: str) -> int:
    s = s.split()
    return len(s[-1])

print(lenghtOfLastWord("of of offof"))