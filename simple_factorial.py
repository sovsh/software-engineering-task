def fact(n):
    if n < 0:
        return 0
    fact = 1
    
    for i in range(1, n+1):
        fact = fact * i
    
    print("The factorial of", n, "is : ", end="")
    print(fact)

    return fact