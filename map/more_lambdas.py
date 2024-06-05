anon = lambda x: x * 2  # Not PEP 8 complaint!!!

def double(x):
    return x * 2

# lambda functions have no name
print(anon)
# lambda functions can only contain one expression (no code blocks)
# but can have multiple parameters
print(lambda x: x * 2)
print(double)

print(anon(7))
print(double(7))