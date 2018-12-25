# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
print(f)


# # re-declaring the variable works
f = "abc"
print(f)


# # ERROR: variables of different types cannot be combined
print("this is string " + str(123))


# Global vs. local variables in functions
def someFunction():
    global f  # make this f as global
    f="xyz"
    print(f)

someFunction()  # prints xyz
print(f)    # print last value of global f

del f # delete global f
print(f) # throw an error since we have deleted global variable f
