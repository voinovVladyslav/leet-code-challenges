def calPoints(ops: list[str]) -> int:
    res = []
    for i in ops:
        if i == "C":
            res.pop(-1)

        elif i == "+":
            res.append(res[-1] + res[-2])

        elif i == "D":
            res.append(res[-1] * 2)

        else:
            res.append(int(i))
    return sum(res)


print(calPoints(["5","-2","4","C","D","9","+","+"]))