def div(x,y):
    print(x/y)


try:
    div(2,1)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print("something went wrong")


