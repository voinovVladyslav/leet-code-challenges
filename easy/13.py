def romanToInt(a: str) -> int:
    x = list(a)
    
    for i in range(len(x)):
        if x[i] == "I":
            x[i] = 1
        elif x[i] == "V":
            x[i] = 5
        elif x[i] == "X":
            x[i] = 10
        elif x[i] == "L":
            x[i] = 50
        elif x[i] == "C":
            x[i] = 100
        elif x[i] == "D":
            x[i] = 500
        else:
            x[i] = 1000
    
    sum = 0
    
    for i in range(len(x)):
        if i == len(x)-1:
            sum += x[i]
            continue
        elif x[i] < x[i+1]:
            sum -= x[i]
        else:
            sum += x[i]
        
    return sum

print(romanToInt('IV'))