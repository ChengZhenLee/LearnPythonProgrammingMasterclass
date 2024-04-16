def spam1():

    def spam2():

        def spam3():
            z = " even more spam"
            # y is a non-local variable initialized in spam2
            # that is used in spam3, thus being added to the 
            # local namespace in spam3
            z += y
            # prints z, y (why has been added to local namespace)
            print("In spam3, locals are {}".format(locals()))
            return z
        
        y = " more spam" # y must exist before spam3 is called
        y += spam3()    # do not combine these assignments
        # prints y, spam3 
        print("In spam2, locals are {}".format(locals()))
        return y
    
    x = "spam"  # + spam2()  x must exist before spam2 is called
    x += spam2()    # do not combines these assignments
    # prints x, spam2
    print("In spam1, locals are {}".format(locals()))
    return x

print(spam1())

# Locals and globals are exactly the same as all variables are
# contained in the functions
print(locals())
print(globals())

# Python scopes
# LEGB
#   Local
#   Enclosing
#   Global
#   Built-in