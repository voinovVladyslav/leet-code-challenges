def solution(x):
    prefix = ""
    
    for i in x[0]:
        cond = True
        for j in x:
            if not j.startswith(prefix + i):
                cond = False
        if cond:
           prefix += i

    return prefix
            
print(solution(["123","12345","12"]))