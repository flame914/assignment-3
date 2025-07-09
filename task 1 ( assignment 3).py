def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        x= x * (factorial(x-1))
        return x
result=factorial(5)
print(result)
