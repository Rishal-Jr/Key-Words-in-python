for x in range(10):
    if x%2==0:
        print("Twist",x)
    elif x%7==0:
        pass
    elif x%5==0:
        print("Fizz",x)
    elif x%3==0:
        print("Buzz",x)
    else:
        print(x)