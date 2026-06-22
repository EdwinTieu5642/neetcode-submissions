def add_two_numbers() -> int:
    string_num = input()
    temp = string_num.split(",")
    temp2 = []

    for i in temp:
        temp2.append(int(i))
    
    return temp2[0] + temp2[1]
    
# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
