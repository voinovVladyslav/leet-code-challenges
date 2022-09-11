def search(m: list[list[int]], target: int) -> bool:
    for i in m:
        if target in i:
            return True
    return False
            
x = [[1,3,5,7],[10,11,16,23],[25,29,33,34]]
print(search(x, 1))