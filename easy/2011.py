def finalValue(operations: list[str]) -> int:
    x = 0
    for i in operations:
        if i.startswith("++") or i.endswith("++"):
            x += 1
        else:
            x -= 1
    return x

print(finalValue(["--X","X++","X++"]))