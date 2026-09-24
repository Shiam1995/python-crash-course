# creating test

# and, or, xor, nor, nand, not, buffer

a = 0
b = 0


print( "A  = 0, B = 0")
if ( a == 0 and b == 0):
    print ("And output = 0")

if ( a == 0 or b == 0):
    print ("Or output = 0")

if ( a == 0):
    print("Not A = 1")

if ( b == 0):
    print("Not B = 0")

if ( a == 0 and b == 0):
    print("NOR output = 1")

a = 1

print( "A  = 1, B = 0")
if ( a == 1 and b == 0):
    print ("And output = 0")

if ( a == 1 or b == 0):
    print ("Or output = 1")

if ( a == 1):
    print("Not A = 0")

if ( b == 0):
    print("Not B = 0")

if ( a == 1 and b == 0):
    print("NOR output = 0")