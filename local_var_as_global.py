var="Good"          # Global variable

def show():         # definition function
    global var1
    var1="morning"  # local variable
    print("In function global var is::",var)
    print("In function var1 is::",var1)

show()              # function calling
print("global var is::",var)
print("Outside function var1 is::",var1)

'''
In function global var is:: Good
In function var1 is:: morning
global var is:: Good
Outside function var1 is:: morning
'''