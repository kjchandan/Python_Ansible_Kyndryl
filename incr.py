factor = 10
def incr(basic):
    global factor
    print(basic * factor)
    factor=15

print(factor)
incr(1000)
print(factor)
