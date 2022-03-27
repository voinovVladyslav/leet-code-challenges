def isValid(s: str) -> bool:
    if len(s) % 2 == 1:
        return False
    prev = ''
    
    while prev != s and len(s) != 0: 
        prev = s
        s = s.replace('()', '--')
        s = s.replace('[]','--')
        s = s.replace('{}','--')

        t = s.split("--")
        s = "".join(t)
        print(s)
        
    if len(s) == 0:
        return True
    else:
        return False

print(isValid("({(())}[[]]())))"))