ordinal = ['st', 'nd', 'rd', 'th']
nums = [1,2,3,4,5,6,7,8,9]

for num in nums:
    if num == 1:
        print("1" + ordinal[0])
    elif num == 2:
        print("2" + ordinal[1])
    elif num == 3:
        print("3" + ordinal[2])
    else:
        print( str(num) + str(ordinal[3]))
