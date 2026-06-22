from typing import List

def read_integers() -> List[int]:
    value = input()
    result = value.split(",")
    final = []
    for i in range(len(result)):
        temp = result[i]
        temp2 = int(result[i])
        final.append(temp2)
    return final
    
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
