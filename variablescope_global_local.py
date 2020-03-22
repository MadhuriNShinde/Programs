num1=10         # num1 is the global variable
print("Global variable::",num1)

def func(num2): # num2 is a function parameter 
    print("in function local variable num2::",num2)
    num3=30     # num3 is a local variable
    print("in function local variable num3::",num3)

func(20)        # 20 is passed in func()
print("num1 is ::",num1)
print("num3 outside function ::",num3)