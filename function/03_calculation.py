operator = input()
a = int(input())
b = int(input())
def solve(a, b, operator):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "devide":
        result = int(a/b)
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result
result = solve(a, b, operator)
print(result)