def factorial(number):
    val = 1
    for i in range(1, number+1):
        val *= i

    return val


a, b = map(int, input().split())

print(factorial(a)//factorial(b)//factorial(a-b))


