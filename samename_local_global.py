#same name local and global
var="Good"          # Global variable

def show():
    var="morning"  # local variable
    print("In function var is::",var)

show()
print("Outside function var is::",var)


'''
In function var is:: morning
Outside function var is:: Good
'''