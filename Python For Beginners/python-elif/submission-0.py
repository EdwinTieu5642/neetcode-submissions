def check_range(num: int) -> str:
    string = ""
    if num < 0:
        string = "negative"
    elif num == 0:
        string = "zero"
    elif num > 0 and num < 10:
        string = "positive single digit"
    elif num >= 10:
        string = "positive multi digit"
    return string
  
# don't modify code below this line
print(check_range(-10))
print(check_range(0))
print(check_range(9))
print(check_range(1000))
