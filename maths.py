def calc(m, n):
    r = m*n
    t = r//2
    result = t%7
    return result
def oneLineCalc(m,n):
    return ((m*n)//2)%7

print("Pythonic Function")
print(calc(6,7))
print(calc(5,5))
print("One Line Function")
print(oneLineCalc(6,7))
print(oneLineCalc(5,5))
print("Lambda")
result = lambda m, n: ((m*n)//2)%7
print(result(6,7))
print(result(5,5))