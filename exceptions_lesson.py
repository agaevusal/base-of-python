def f(x,y):
    try:
        Result = x//y
    except ZeroDivisionError:
        print('error: ZeroDivisionError')
    else:
        print('Result is', Result)
    finally:
        print('finally')

f(4,'a')